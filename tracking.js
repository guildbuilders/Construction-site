/* Guild Builders — dataLayer for GTM / server-side GTM.
   Implements the tracking spec the media partner supplied (generate_lead with
   normalised user_data for Google Ads Enhanced Conversions and Meta CAPI
   advanced matching, form_error, and micro conversions), translated from the
   Next.js/React version in that document to this site, which is static HTML
   with forms that POST to formsubmit.co.

   This file only PUSHES to the dataLayer. It configures nothing and sends
   nothing to Google directly - the tags that act on these events live in GTM.
   The hardcoded gtag layer still owns Ads and GA4 until it is stripped; see
   tools/strip_gtag.py. Nothing here fires a conversion, so it cannot double
   count while both exist. */
(function () {
  "use strict";

  window.dataLayer = window.dataLayer || [];

  function push(payload) {
    /* Strip undefined so the dataLayer object matches the spec's "omits empty
       fields" rule rather than carrying keys GTM would read as empty strings. */
    Object.keys(payload).forEach(function (k) {
      if (payload[k] === undefined) delete payload[k];
    });
    window.dataLayer.push(payload);
  }

  function eventId(prefix) {
    return prefix + "_" + Date.now() + "_" + Math.random().toString(36).substring(2, 9);
  }

  function cookie(name) {
    var m = document.cookie.match(new RegExp("(^|;\\s*)(" + name + ")=([^;]*)"));
    return m ? decodeURIComponent(m[3]) : undefined;
  }

  function baseContext(leadSource) {
    return {
      page_path: location.pathname,
      page_url: location.href,
      referrer: document.referrer || "(direct)",
      lead_source: leadSource || undefined
    };
  }

  /* E.164, which is what both Enhanced Conversions and Meta advanced matching
     expect. US numbers only: everything this site takes is San Diego County. */
  function e164(raw) {
    if (!raw) return undefined;
    var d = String(raw).replace(/\D/g, "");
    if (d.length === 11 && d.charAt(0) === "1") return "+" + d;
    if (d.length === 10) return "+1" + d;
    return d ? "+" + d : undefined;
  }

  function trimmed(v) {
    var s = (v || "").trim();
    return s || undefined;
  }

  function formOf(el) {
    return el.closest ? el.closest("form[data-form-name]") : null;
  }

  function field(form, name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? el.value : "";
  }

  /* ---------- 1. Lead capture ----------
     The forms POST cross-origin to formsubmit.co, which answers with a redirect
     to the thank-you page, so the browser is already leaving when submit fires.
     A generate_lead push here would race that navigation and GTM would often
     lose it - and any tag that needs to send a request would lose it more
     often. So the lead is stashed and pushed on the thank-you page, which loads
     normally and gives every tag a full page lifetime to fire.

     sessionStorage survives the round trip: the tab is the same one and the
     origin it comes back to is the origin it left. */
  var STASH = "gb_lead";

  function captureLead(form) {
    var first = trimmed(field(form, "first_name"));
    var last = trimmed(field(form, "last_name"));

    /* The contact form takes one "name" field rather than two. */
    if (!first && !last) {
      var whole = trimmed(field(form, "name"));
      if (whole) {
        var parts = whole.split(/\s+/);
        first = parts.shift();
        last = parts.length ? parts.join(" ") : undefined;
      }
    }

    var email = trimmed(field(form, "email"));
    var address = {
      first_name: first,
      last_name: last,
      city: trimmed(field(form, "city")),
      region: trimmed(field(form, "region")),
      postal_code: trimmed(field(form, "postal_code")),
      country: "US"
    };
    var hasAddress = Object.keys(address).some(function (k) {
      return k !== "country" && address[k];
    });

    var payload = {
      event: "generate_lead",
      /* Generated here rather than on the thank-you page so the id belongs to
         the submission itself. It is the deduplication key between the browser
         tag and the CAPI tag, so it has to be the same value for both. */
      event_id: eventId("lead"),
      form_name: form.getAttribute("data-form-name") || "form",
      currency: "USD",
      lead_captured: true
    };

    var ctx = baseContext(form.getAttribute("data-lead-source") || field(form, "lead_source"));
    Object.keys(ctx).forEach(function (k) { payload[k] = ctx[k]; });

    payload.user_data = {
      email_address: email ? email.toLowerCase() : undefined,
      phone_number: e164(field(form, "phone")),
      address: hasAddress ? address : undefined,
      fbp: cookie("_fbp"),
      fbc: cookie("_fbc")
    };

    try {
      sessionStorage.setItem(STASH, JSON.stringify(payload));
    } catch (e) {
      /* Private mode or storage full. The thank-you page still pushes
         generate_lead, just without user_data, so the conversion is not lost -
         only the enhanced matching is. */
    }
  }

  /* ---------- 2. Thank-you flush ----------
     Pushed on every thank-you view, with or without a stash, so the event
     count matches the conversion the page already reports to Ads. A view with
     no stash (someone opening the URL directly, or a new tab) carries
     lead_captured: false so it can be filtered in GTM if that is ever wanted. */
  function flushLead() {
    var raw = null;
    try {
      raw = sessionStorage.getItem(STASH);
      sessionStorage.removeItem(STASH);
    } catch (e) { /* storage unavailable */ }

    if (raw) {
      var parsed;
      try {
        parsed = JSON.parse(raw);
      } catch (e) {
        parsed = null;
      }
      if (parsed) {
        /* Where the conversion is being reported from, alongside the page the
           form was actually on, which stays in page_path/page_url. */
        parsed.thank_you_path = location.pathname;
        push(parsed);
        return;
      }
    }

    var payload = {
      event: "generate_lead",
      event_id: eventId("lead"),
      form_name: document.body.getAttribute("data-form-name") || "unknown",
      currency: "USD",
      lead_captured: false,
      thank_you_path: location.pathname
    };
    var ctx = baseContext();
    Object.keys(ctx).forEach(function (k) { payload[k] = ctx[k]; });
    push(payload);
  }

  /* ---------- 3. Micro conversions ----------
     One delegated listener rather than a handler per link, so numbers CallRail
     swaps in and any link added later are covered without touching this file. */
  function microConversion(event, target, label) {
    push({
      event: event,
      event_id: eventId("micro"),
      interaction_target: target,
      link_label: label || target,
      page_path: location.pathname,
      page_url: location.href,
      referrer: document.referrer || "(direct)"
    });
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var label = (a.innerText || "").trim();

    if (href.indexOf("tel:") === 0) {
      microConversion("click_to_call", href.slice(4).trim(), label);
    } else if (href.indexOf("mailto:") === 0) {
      microConversion("click_to_email", href.slice(7).trim(), label);
    } else if (href.indexOf("calendar.app.google") !== -1) {
      /* Not in the partner's document. Bookings are a lead the forms never
         see, so they need an event of their own if they are ever to be counted
         as a conversion. */
      microConversion("booking_click", href, label);
    } else if (/\.(pdf|xlsx?|docx?|zip)(\?.*)?$/i.test(href)) {
      microConversion("file_download", href, label || "Asset Download");
    }
  });

  /* ---------- 4. Form errors ----------
     The forms validate through required/type attributes rather than script, so
     the browser's own invalid event is the signal. Capture phase because
     invalid does not bubble. */
  document.addEventListener("invalid", function (e) {
    var form = formOf(e.target);
    if (!form) return;
    var v = e.target.validity;
    var type = v.valueMissing ? "missing_required"
      : (v.typeMismatch || v.patternMismatch) ? "invalid_format"
      : v.tooShort || v.tooLong ? "invalid_length"
      : "invalid";
    push({
      event: "form_error",
      form_name: form.getAttribute("data-form-name") || "form",
      field_name: e.target.getAttribute("name") || e.target.id || "unknown",
      error_type: type,
      page_path: location.pathname,
      page_url: location.href,
      referrer: document.referrer || "(direct)",
      lead_source: form.getAttribute("data-lead-source") || undefined
    });
  }, true);

  document.addEventListener("submit", function (e) {
    var form = e.target;
    if (!form || !form.getAttribute || !form.getAttribute("data-form-name")) return;
    captureLead(form);
  }, true);

  if (document.body && document.body.classList.contains("gb-thanks")) {
    flushLead();
  }
})();
