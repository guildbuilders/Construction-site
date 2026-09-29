/* Same-origin tagging proxy for the Stape server-side GTM container.
   PREPARED BUT NOT WIRED IN. wrangler.jsonc still deploys this site as a
   static-assets Worker with no script; flipping this on means adding
   "main": "worker/index.js" and a binding for the assets. Two things are
   needed before that is worth doing, both from the Stape admin:

     TAGGING_HOST  the tagging server hostname - the custom subdomain if one
                   has been created (recommended: it is what makes the loader
                   first-party and the cookies long-lived), otherwise the
                   default xxxx.stape.io host
     STAPE_HOST    only used with the DEFAULT stape.io host, where Stape needs
                   to be told which site the traffic belongs to

   Why this rather than the second Worker the Stape article describes: this
   site is already a Worker on this zone, so a separate Worker with a route on
   the same hostname is a precedence question nobody wants to debug in
   production. Doing the proxy here also lets the two headers be set in code,
   which removes both Request Header Transform Rules from the setup, and the
   Configuration Rule with them - there is no Cloudflare-to-origin leg to force
   to Full SSL when the request is made by fetch() to an https URL.

   Reference: https://stape.io/helpdesk/documentation/how-to-use-same-origin-through-cloudflare */

/* The first-party path the browser sees. Must match the server_container_url
   in the web container's Google tag and the Custom Loader path in Stape.

   Not /metrics, which is what the Stape article uses: Stape's own custom
   domain dialog lists "metrics" among the words to avoid because blocklists
   match on them, and a path copied verbatim out of their documentation is the
   easiest possible pattern to match. The whole point of same origin is to be
   unremarkable. */
const TAGGING_PATH = "/edge";

/* Custom subdomain, CNAME to usv.stape.io, DNS-only in Cloudflare. The browser
   never sees this host - it talks to guildbuildersgroup.com/edge and this
   Worker makes the onward call. */
const TAGGING_HOST = "edge.guildbuildersgroup.com";

/* null because TAGGING_HOST is a custom subdomain. Stape only needs this
   header to disambiguate traffic arriving at a shared stape.io host. */
const STAPE_HOST = null;


/* ---------------------------------------------------------------------------
   LEAD CAPTURE.  Added 2026-09-29, the day FormSubmit's backend started
   returning 500 to every POST - including to endpoints that belong to nobody,
   which is how we knew it was their pipeline and not this account. Every form
   on the site posted there, so every form lead was being dropped silently:
   the visitor saw a FormSubmit error page instead of the thank-you page, and
   because /thank-you never loaded, generate_lead never fired and Google Ads
   recorded nothing either.

   The rule this is built around: STORE FIRST, NOTIFY SECOND. The KV write is
   awaited before the visitor is redirected, so a lead exists the moment it
   arrives. Email is best-effort on top. If Resend is down, or the key is
   missing, or the address is wrong, the lead is still on disk and can be
   replayed - which is exactly what could not be done with the old setup.

   The visitor still lands on the site's own thank-you page, so tracking.js
   still pushes generate_lead and the Ads conversion still fires. That path is
   unchanged on purpose.

   Env:
     LEADS            KV namespace, bound in wrangler.jsonc
     RESEND_API_KEY   secret. Absent = capture only, no email, no error.
     LEAD_TO          where notifications go. Comma-separated for several.
     LEAD_FROM        verified sender on the Resend domain.
--------------------------------------------------------------------------- */

const LEAD_PATH = "/lead";

/* Redirect targets have to be ours. An attacker can post a form at this
   endpoint with any _next they like, and without this check the site would
   happily bounce people to their URL wearing our domain's reputation. */
const ALLOWED_REDIRECT_HOSTS = new Set([
  "guildbuildersgroup.com",
  "www.guildbuildersgroup.com",
]);

const DEFAULT_NEXT = "https://guildbuildersgroup.com/thank-you";

function safeNext(raw) {
  if (!raw) return DEFAULT_NEXT;
  try {
    const u = new URL(raw, "https://guildbuildersgroup.com");
    if (u.protocol !== "https:") return DEFAULT_NEXT;
    if (!ALLOWED_REDIRECT_HOSTS.has(u.hostname)) return DEFAULT_NEXT;
    return u.toString();
  } catch (e) {
    return DEFAULT_NEXT;
  }
}

function esc(s) {
  return String(s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}

/* Field order for the email. Anything not named here still gets through, it
   just lands after these, so adding a field to a form needs no change here. */
const FIELD_ORDER = [
  "name", "first_name", "last_name", "email", "phone", "zip", "message",
  "lead_source", "gclid", "utm_source", "utm_medium", "utm_campaign",
  "utm_term", "utm_content",
];

function orderFields(fields) {
  const keys = Object.keys(fields);
  const known = FIELD_ORDER.filter((k) => keys.includes(k));
  const rest = keys.filter((k) => !FIELD_ORDER.includes(k)).sort();
  return known.concat(rest);
}

function emailHtml(record) {
  const rows = orderFields(record.fields)
    .map(function (k) {
      return (
        '<tr><td style="padding:6px 12px;border:1px solid #d8dee8;background:#f6f8fb;' +
        'font-family:system-ui,sans-serif;font-size:14px;color:#0f1c2e;white-space:nowrap">' +
        esc(k.replace(/_/g, " ")) +
        '</td><td style="padding:6px 12px;border:1px solid #d8dee8;font-family:system-ui,' +
        'sans-serif;font-size:14px;color:#0f1c2e">' +
        esc(record.fields[k]).replace(/\n/g, "<br />") +
        "</td></tr>"
      );
    })
    .join("");

  return (
    '<div style="font-family:system-ui,sans-serif;color:#0f1c2e">' +
    "<p style=\"font-size:15px\"><strong>New enquiry from the Guild Builders website.</strong></p>" +
    '<table style="border-collapse:collapse;margin:12px 0">' + rows + "</table>" +
    '<p style="font-size:12px;color:#66707f">' +
    "Form: " + esc(record.form_name) + " &middot; Page: " + esc(record.page) + "<br />" +
    "Received: " + esc(record.received) + " &middot; Reference: " + esc(record.id) +
    "</p></div>"
  );
}

async function sendEmail(env, record) {
  if (!env.RESEND_API_KEY) return { sent: false, reason: "no api key configured" };
  const to = (env.LEAD_TO || "").split(",").map((s) => s.trim()).filter(Boolean);
  if (!to.length) return { sent: false, reason: "no LEAD_TO configured" };

  const body = {
    from: env.LEAD_FROM || "Guild Builders Website <leads@guildbuildersgroup.com>",
    to: to,
    subject: record.subject,
    html: emailHtml(record),
  };
  /* So hitting reply in the inbox answers the customer rather than the robot. */
  if (record.fields.email && /.+@.+\..+/.test(record.fields.email)) {
    body.reply_to = record.fields.email;
  }

  try {
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: "Bearer " + env.RESEND_API_KEY,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    const text = await res.text();
    return res.ok
      ? { sent: true, provider_response: text.slice(0, 300) }
      : { sent: false, reason: "http " + res.status, provider_response: text.slice(0, 300) };
  } catch (e) {
    return { sent: false, reason: String(e).slice(0, 300) };
  }
}

async function handleLead(request, env, ctx) {
  if (request.method !== "POST") {
    return Response.redirect("https://guildbuildersgroup.com/contact", 303);
  }

  let form;
  try {
    form = await request.formData();
  } catch (e) {
    return Response.redirect(DEFAULT_NEXT, 303);
  }

  const fields = {};
  let honey = "";
  let next = "";
  let subject = "";
  for (const [k, v] of form.entries()) {
    const val = typeof v === "string" ? v.trim() : "";
    if (k === "_honey") { honey = val; continue; }
    if (k === "_next") { next = val; continue; }
    if (k === "_subject") { subject = val; continue; }
    if (k.charAt(0) === "_") continue;      /* other FormSubmit controls */
    if (val) fields[k] = val.slice(0, 5000);
  }

  const target = safeNext(next);

  /* Bots fill hidden inputs. Give them the same redirect a person gets, so
     nothing tells them they were caught, but store nothing and send nothing. */
  if (honey) return Response.redirect(target, 303);

  const now = new Date();
  const id = now.toISOString() + "-" + crypto.randomUUID().slice(0, 8);
  const record = {
    id: id,
    received: now.toISOString(),
    form_name: form.get("form_name") || request.headers.get("X-Form-Name") || "unknown",
    subject: subject || "New Guild Builders website enquiry",
    page: request.headers.get("Referer") || "",
    ip: request.headers.get("CF-Connecting-IP") || "",
    country: (request.cf && request.cf.country) || "",
    user_agent: request.headers.get("User-Agent") || "",
    fields: fields,
  };

  /* Awaited, not fired and forgotten: the lead has to be safe on disk before
     this request is allowed to finish. */
  if (env.LEADS) {
    await env.LEADS.put("lead:" + id, JSON.stringify(record));
  }

  /* Email runs after the response is on its way, so a slow provider never
     makes the visitor wait on the thank-you page. */
  const notify = sendEmail(env, record).then(async function (result) {
    if (env.LEADS) {
      record.delivery = result;
      await env.LEADS.put("lead:" + id, JSON.stringify(record));
    }
  });
  if (ctx && ctx.waitUntil) ctx.waitUntil(notify);

  return Response.redirect(target, 303);
}


/* ---------------------------------------------------------------------------
   PRIVATE LEAD INBOX.  /leads?key=<token>

   A safety net, not a CRM: if an email provider fails the way FormSubmit did,
   every lead is still here and still readable. Read only, no deleting, so
   this page can never be the reason a lead disappears.

   Access is a single token in LEADS_VIEW_KEY (a Worker secret, never the
   repo). Supplying it once sets a cookie, so the link only has to be used
   the first time on a given device. A wrong token or no token gets the same
   404 the rest of the site gives, which tells a scanner nothing about whether
   the path exists.
--------------------------------------------------------------------------- */

const LEADS_VIEW_PATH = "/leads";
const LEADS_COOKIE = "gb_leads";

/* Length check first so the comparison below cannot leak the length, then a
   full-width compare that does not stop at the first wrong character. */
function tokenMatches(given, expected) {
  if (!given || !expected || given.length !== expected.length) return false;
  let diff = 0;
  for (let i = 0; i < given.length; i++) {
    diff |= given.charCodeAt(i) ^ expected.charCodeAt(i);
  }
  return diff === 0;
}

function cookieValue(header, name) {
  if (!header) return "";
  const parts = header.split(";");
  for (const part of parts) {
    const eq = part.indexOf("=");
    if (eq === -1) continue;
    if (part.slice(0, eq).trim() === name) return part.slice(eq + 1).trim();
  }
  return "";
}

function fmtWhen(iso) {
  try {
    return new Date(iso).toLocaleString("en-US", {
      timeZone: "America/Los_Angeles",
      weekday: "short", month: "short", day: "numeric",
      hour: "numeric", minute: "2-digit",
    });
  } catch (e) { return iso; }
}

function leadCard(record) {
  const f = record.fields || {};
  const name = [f.name, [f.first_name, f.last_name].filter(Boolean).join(" ")]
    .filter(Boolean)[0] || "No name given";

  const contact = [];
  if (f.phone) {
    contact.push('<a class="btn" href="tel:' + esc(f.phone.replace(/[^0-9+]/g, "")) +
      '">Call ' + esc(f.phone) + "</a>");
  }
  if (f.email) {
    contact.push('<a class="btn ghost" href="mailto:' + esc(f.email) + '">' + esc(f.email) + "</a>");
  }

  const skip = { name: 1, first_name: 1, last_name: 1, phone: 1, email: 1, form_name: 1 };
  const rest = orderFields(f)
    .filter((k) => !skip[k])
    .map((k) =>
      '<div class="row"><span class="k">' + esc(k.replace(/_/g, " ")) + "</span>" +
      '<span class="v">' + esc(f[k]).replace(/\n/g, "<br />") + "</span></div>")
    .join("");

  const d = record.delivery;
  const badge = !d
    ? '<span class="badge wait">email pending</span>'
    : d.sent
      ? '<span class="badge ok">emailed</span>'
      : '<span class="badge bad">email failed: ' + esc(d.reason || "unknown") + "</span>";

  return (
    '<article class="lead">' +
    '<header><h2>' + esc(name) + "</h2>" +
    '<time>' + esc(fmtWhen(record.received)) + "</time></header>" +
    (contact.length ? '<div class="actions">' + contact.join("") + "</div>" : "") +
    (rest ? '<div class="fields">' + rest + "</div>" : "") +
    '<footer>' + esc(record.form_name || "unknown form") + " &middot; " + badge + "</footer>" +
    "</article>"
  );
}

function leadsPage(records) {
  const cards = records.length
    ? records.map(leadCard).join("")
    : '<p class="empty">No leads stored yet. Anything submitted on the site appears here the moment it arrives, whether or not the email goes out.</p>';

  return '<!doctype html><html lang="en"><head><meta charset="utf-8" />' +
    '<meta name="viewport" content="width=device-width, initial-scale=1" />' +
    '<meta name="robots" content="noindex, nofollow" />' +
    "<title>Leads | Guild Builders</title><style>" +
    ":root{color-scheme:light}" +
    "*{box-sizing:border-box}" +
    "body{margin:0;background:#eef1f6;color:#0f1c2e;font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}" +
    ".wrap{max-width:720px;margin:0 auto;padding:20px 16px 60px}" +
    "h1{font-size:20px;margin:0 0 4px}" +
    ".sub{color:#66707f;font-size:13px;margin:0 0 20px}" +
    ".lead{background:#fff;border:1px solid #dde3ec;border-radius:12px;padding:16px;margin:0 0 14px}" +
    ".lead header{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}" +
    ".lead h2{font-size:17px;margin:0}" +
    ".lead time{color:#66707f;font-size:12px;white-space:nowrap}" +
    ".actions{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}" +
    ".btn{display:inline-block;background:#14243a;color:#fff;text-decoration:none;padding:9px 14px;border-radius:8px;font-size:14px;font-weight:600}" +
    ".btn.ghost{background:#fff;color:#14243a;border:1px solid #c7d0de;font-weight:500}" +
    ".fields{border-top:1px solid #eef1f6;padding-top:10px}" +
    ".row{display:flex;gap:10px;padding:3px 0;font-size:14px}" +
    ".k{color:#66707f;min-width:104px;text-transform:capitalize;flex:none}" +
    ".v{color:#0f1c2e;overflow-wrap:anywhere}" +
    "footer{margin-top:12px;padding-top:10px;border-top:1px solid #eef1f6;color:#66707f;font-size:12px}" +
    ".badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:600}" +
    ".badge.ok{background:#e4f5ea;color:#1c6b3a}" +
    ".badge.bad{background:#fdeaea;color:#a12626}" +
    ".badge.wait{background:#fdf3e2;color:#8a5a12}" +
    ".empty{background:#fff;border:1px solid #dde3ec;border-radius:12px;padding:24px;color:#66707f}" +
    "</style></head><body><div class=\"wrap\">" +
    "<h1>Leads</h1>" +
    '<p class="sub">' + records.length + (records.length === 1 ? " lead" : " leads") +
    " stored, newest first. Times are Pacific.</p>" +
    cards + "</div></body></html>";
}

async function handleLeadsView(request, env) {
  const notFound = () =>
    new Response("Not found", { status: 404, headers: { "Content-Type": "text/plain" } });

  if (request.method !== "GET") return notFound();
  if (!env.LEADS_VIEW_KEY || !env.LEADS) return notFound();

  const url = new URL(request.url);
  const fromQuery = url.searchParams.get("key") || "";
  const fromCookie = cookieValue(request.headers.get("Cookie"), LEADS_COOKIE);

  const viaQuery = tokenMatches(fromQuery, env.LEADS_VIEW_KEY);
  if (!viaQuery && !tokenMatches(fromCookie, env.LEADS_VIEW_KEY)) return notFound();

  /* Keys are lead:<ISO timestamp>, so KV's lexicographic order is
     chronological order and reversing gives newest first. */
  const listed = await env.LEADS.list({ prefix: "lead:", limit: 400 });
  const newest = listed.keys.map((k) => k.name).reverse().slice(0, 60);
  const values = await Promise.all(
    newest.map((name) => env.LEADS.get(name, { type: "json" }).catch(() => null))
  );
  const records = values.filter(Boolean);

  const headers = {
    "Content-Type": "text/html; charset=utf-8",
    "Cache-Control": "no-store, private",
    "X-Robots-Tag": "noindex, nofollow",
    "Referrer-Policy": "no-referrer",
  };
  /* Arriving with the key in the URL trades it for a cookie, so the token
     stops travelling in the address bar on every later visit. */
  if (viaQuery) {
    headers["Set-Cookie"] = LEADS_COOKIE + "=" + env.LEADS_VIEW_KEY +
      "; Path=" + LEADS_VIEW_PATH + "; Max-Age=7776000; HttpOnly; Secure; SameSite=Lax";
  }
  return new Response(leadsPage(records), { headers });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === LEAD_PATH) {
      return handleLead(request, env, ctx);
    }

    if (url.pathname === LEADS_VIEW_PATH) {
      return handleLeadsView(request, env);
    }

    const inTaggingPath =
      url.pathname === TAGGING_PATH || url.pathname.startsWith(TAGGING_PATH + "/");

    if (!inTaggingPath) {
      /* Everything else is the site itself, served exactly as it is today. */
      return env.ASSETS.fetch(request);
    }

    /* /metrics/g/collect -> /g/collect on the tagging server. The prefix is a
       routing detail of this site and means nothing to sGTM. */
    const path = url.pathname.slice(TAGGING_PATH.length) || "/";
    const target = "https://" + TAGGING_HOST + path + url.search;

    const proxied = new Request(target, request);
    proxied.headers.set("Host", TAGGING_HOST);
    /* Tells Stape the request arrived through a CDN rather than directly, so
       it reads the client IP from the forwarding headers instead of the
       edge's. Without it every hit looks like it came from Cloudflare. */
    proxied.headers.set("X-From-Cdn", "cf-stape");
    if (STAPE_HOST) {
      proxied.headers.set("X-Stape-Host", STAPE_HOST);
    }

    /* Measurement traffic must never be served from cache: these are
       per-visitor beacons, and a cached response would attribute one person's
       hit to another. */
    return fetch(proxied, { cf: { cacheTtl: 0, cacheEverything: false } });
  },
};
