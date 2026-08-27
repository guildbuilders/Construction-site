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

  /* ---------- 1b. Ad attribution ----------
     The forms POST to formsubmit.co, which emails whatever named fields the
     form carries. Until now the only source field was the page's static
     lead_source, so a lead said which landing page produced it but never which
     campaign, ad group or keyword. These stamp the click ids and utm
     parameters onto every lead form so the email answers that, and onto
     generate_lead so the same values reach GA4, Ads and Meta.

     Read on load and stashed, because a visitor can arrive on an ad URL,
     browse to another page and submit there, by which point the query string
     is long gone. */
  var ATTR_STASH = "gb_attr";
  var ATTR_KEYS = [
    "gclid", "gbraid", "wbraid",
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"
  ];

  function attribution() {
    var found = {};
    var any = false;

    try {
      var q = new URLSearchParams(location.search);
      for (var i = 0; i < ATTR_KEYS.length; i++) {
        var v = q.get(ATTR_KEYS[i]);
        if (v) {
          v = v.trim();
          if (v) {
            found[ATTR_KEYS[i]] = v;
            any = true;
          }
        }
      }
    } catch (e) { /* no URLSearchParams; fall through to the stash */ }

    /* A fresh set of parameters replaces the stash rather than merging into
       it, so a second ad click in the same tab is not credited to the first. */
    if (any) {
      try {
        sessionStorage.setItem(ATTR_STASH, JSON.stringify(found));
      } catch (e) { /* private mode; this page still stamps its own values */ }
      return found;
    }

    try {
      var raw = sessionStorage.getItem(ATTR_STASH);
      if (raw) {
        var parsed = JSON.parse(raw);
        if (parsed && typeof parsed === "object") {
          for (var k = 0; k < ATTR_KEYS.length; k++) {
            var key = ATTR_KEYS[k];
            if (typeof parsed[key] === "string" && parsed[key]) found[key] = parsed[key];
          }
        }
      }
    } catch (e) { /* unreadable stash; carry on without it */ }

    /* Google's own cookie, last resort: someone who clicked an ad earlier
       still carries it once the query string is gone. The value is
       GCL.<timestamp>.<gclid>, so the click id is the final segment. */
    if (!found.gclid) {
      var aw = cookie("_gcl_aw");
      if (aw) {
        var parts = aw.split(".");
        var last = parts[parts.length - 1];
        if (parts.length > 2 && last) found.gclid = last;
      }
    }

    return found;
  }

  /* Written into the form as hidden fields on load rather than injected during
     submit, so the values are part of the form before anything can race the
     handler, and a submit that bypasses the listener still carries them. */
  function stampForms() {
    var attr = attribution();
    var keys = Object.keys(attr);
    if (!keys.length) return;

    var forms = document.querySelectorAll("form[data-form-name]");
    for (var i = 0; i < forms.length; i++) {
      for (var j = 0; j < keys.length; j++) {
        var name = keys[j];
        /* Never clobber a field the page already defines. */
        if (forms[i].querySelector('[name="' + name + '"]')) continue;
        var input = document.createElement("input");
        input.type = "hidden";
        input.name = name;
        input.value = attr[name];
        forms[i].appendChild(input);
      }
    }
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

    /* The same values the hidden fields carry, so the dataLayer event and the
       lead email agree about where the lead came from. */
    var attr = attribution();
    Object.keys(attr).forEach(function (k) { payload[k] = attr[k]; });

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
    } else if (href.indexOf("calendar.app.google") !== -1 || /(^|\/)book(\.html)?$/.test(href.split("?")[0])) {
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

  /* ---------- 5. Confirmed bookings ----------
     Only booking-confirmed.html carries this class, and the only way to reach
     that page is the scheduler redirecting there once an appointment is
     actually on the calendar. So booking_click is intent and this is the
     booking, which is the difference that lets Ads bid on the real thing.

     Schedulers put the invitee's details in the redirect query string. Where
     they do, they go into user_data for Enhanced Conversions, and then the
     query string is wiped from the address bar: an email sitting in a URL ends
     up in analytics page paths, browser history and any link the visitor
     shares, and none of those are places it belongs. */
  /* Called by the Cal.com embed on /book the moment a booking completes. The
     embed hands over a payload whose shape Cal.com owns and can change, so
     nothing here assumes a path: it walks the object for the first email and
     name it can find, and records which keys it actually saw so the mapping can
     be checked against a real booking without a customer's address being
     written anywhere it should not be. */
  var BOOKING_STASH = "gb_booking";

  /* Never descends into `organizer`. That block is us, not the customer, and a
     walk looking for "the first name or email in the object" will happily
     return ours. Guarding the email alone was not enough: a payload with no
     attendee still handed back the organizer's NAME as the booker's. */
  var NOT_THE_CUSTOMER = { organizer: 1, team: 1, owner: 1, host: 1 };

  function dig(obj, keys, depth) {
    if (!obj || typeof obj !== "object" || (depth || 0) > 4) return undefined;
    for (var i = 0; i < keys.length; i++) {
      var v = obj[keys[i]];
      if (typeof v === "string" && v) return v;
    }
    for (var k in obj) {
      if (!Object.prototype.hasOwnProperty.call(obj, k)) continue;
      if (NOT_THE_CUSTOMER[k]) continue;
      var child = obj[k];
      if (child && typeof child === "object") {
        var found = dig(Array.isArray(child) ? child[0] : child, keys, (depth || 0) + 1);
        if (found) return found;
      }
    }
    return undefined;
  }

  /* The attendee, explicitly. Cal.com's payload also carries an `organizer`
     block, which is us. A generic walk for "the first email in the object"
     could return info@guildbuildersgroup.com depending on key order, and we
     would then hand Google our own address as the customer's for every single
     booking: Enhanced Conversions matching against one address that is never
     the buyer, reported as a healthy setup. So look where the attendee
     actually lives first, and only fall back to walking. */
  function attendee(data) {
    var b = (data && (data.booking || data)) || {};
    var list = b.attendees || b.attendee || (data && data.attendees);
    var first = Array.isArray(list) ? list[0] : list;
    return first && typeof first === "object" ? first : null;
  }

  window.gb_bookingConfirmed = function (data) {
    var who = attendee(data);
    var organizerEmail = data && data.organizer && data.organizer.email;

    var rawEmail = (who && (who.email || who.emailAddress)) ||
      dig(data, ["email", "attendeeEmail", "invitee_email"]);
    var email = rawEmail;
    var whole = (who && (who.name || who.fullName)) ||
      dig(data, ["name", "attendeeName", "invitee_full_name"]);
    /* Cal.com puts custom booking questions in a responses object, so the
       phone can arrive either on the attendee or in there. Same organizer
       guard applies via dig: our own number must never be sent as a
       customer's. */
    var phone = (who && (who.phone || who.phoneNumber || who.attendeePhone || who.attendeePhoneNumber)) ||
      dig(data, ["attendeePhoneNumber", "phone", "phoneNumber", "attendeePhone", "smsReminderNumber", "invitee_phone"]);
    var start = dig(data, ["startTime", "date", "start", "event_start_time"]);

    /* If the only email we could find is the organizer's, it is not a customer
       and must not be sent as one. Better a conversion with no matching data
       than a conversion matched to the wrong person. */
    var droppedAsOrganizer = false;
    if (email && organizerEmail && email.toLowerCase() === String(organizerEmail).toLowerCase()) {
      email = undefined;
      droppedAsOrganizer = true;
    }
    var payload = {
      email: email,
      name: whole,
      phone: phone,
      start: start,
      keys: data && typeof data === "object" ? Object.keys(data).sort().join(",") : ""
    };
    try {
      sessionStorage.setItem(BOOKING_STASH, JSON.stringify(payload));
      /* A breadcrumb that outlives the page, so the mapping can be checked
         after a real booking rather than only in the moment. Field NAMES and
         whether each was found - never the values. Cal.com owns the payload
         shape and can change it; this is how we would notice. */
      localStorage.setItem("gb_last_booking", JSON.stringify({
        at: new Date().toISOString(),
        keys: payload.keys,
        found: { email: !!email, name: !!whole, phone: !!phone, start: !!start },
        fromAttendeeBlock: !!who,
        organizerPresent: !!organizerEmail,
        /* Distinguishes "Cal.com sent no email" from "we dropped it because it
           was the organizer's" - which is what a self-booked test looks like.
           Without this the two are indistinguishable and the honest reading of
           found.email:false is ambiguous. */
        rawEmailPresent: !!rawEmail,
        droppedAsOrganizer: droppedAsOrganizer
      }));
    } catch (e) { /* private mode; the conversion still fires, without matching */ }
    window.location.href = "/booking-confirmed";
  };

  function confirmBooking() {
    var q;
    try {
      q = new URLSearchParams(location.search);
    } catch (e) {
      q = null;
    }
    function param() {
      if (!q) return undefined;
      for (var i = 0; i < arguments.length; i++) {
        var v = q.get(arguments[i]);
        if (v) return v.trim();
      }
      return undefined;
    }

    /* Two ways a booking can arrive here. The embed on /book stashes what
       Cal.com handed it and navigates; a scheduler configured to redirect
       would instead arrive with query parameters. The stash wins when both
       exist, because it came from the booking object rather than a URL. */
    var stashed = null;
    try {
      var raw = sessionStorage.getItem(BOOKING_STASH);
      sessionStorage.removeItem(BOOKING_STASH);
      if (raw) stashed = JSON.parse(raw);
    } catch (e) { /* storage unavailable or unparseable */ }

    var email = (stashed && stashed.email) || param("invitee_email", "email", "attendeeEmail");
    var whole = (stashed && stashed.name) || param("invitee_full_name", "name", "attendeeName", "invitee_name");
    var first = param("invitee_first_name", "firstName");
    var last = param("invitee_last_name", "lastName");
    if (whole && !first && !last) {
      var parts = whole.split(/\s+/);
      first = parts.shift();
      last = parts.length ? parts.join(" ") : undefined;
    }

    var address = { first_name: first, last_name: last, country: "US" };
    var hasName = !!(first || last);

    var payload = {
      event: "booking_confirmed",
      event_id: eventId("booking"),
      currency: "USD",
      booking_start: (stashed && stashed.start) || param("event_start_time", "startTime", "start"),
      scheduler: param("scheduler") || undefined,
      /* False means this page was opened without the scheduler's redirect
         behind it - a refresh, a bookmark, someone with the URL. Filterable in
         GTM, and the reason the Ads action should count One per click. */
      booking_details: !!(email || whole || first),
      /* The NAMES of the query parameters the scheduler sent, never the
         values. Cal.com and Calendly label these differently and the labels
         can change, so this is how we confirm the mapping above actually
         matched after a real booking, without putting a customer's email
         anywhere it should not be. Safe to leave on permanently. */
      booking_param_keys: (stashed && stashed.keys) || (q ? Array.from(q.keys()).sort().join(",") || undefined : undefined),
      booking_source: stashed ? "embed" : (q && q.toString() ? "redirect" : "direct")
    };
    /* baseContext reads location.href, which at this point still has the
       invitee's email in it. The event must not carry that into GA4 or Ads as
       page_url, so the context is built from the path alone. */
    var ctx = baseContext(param("utm_source") || "calendar");
    ctx.page_url = location.origin + location.pathname;
    Object.keys(ctx).forEach(function (k) { payload[k] = ctx[k]; });

    payload.user_data = {
      email_address: email ? email.toLowerCase() : undefined,
      phone_number: e164((stashed && stashed.phone) || param("invitee_phone", "phone", "attendeePhone")),
      address: hasName ? address : undefined,
      fbp: cookie("_fbp"),
      fbc: cookie("_fbc")
    };

    push(payload);

    if (q && location.search && window.history && history.replaceState) {
      history.replaceState(null, "", location.pathname);
    }
  }

  stampForms();

  if (document.body && document.body.classList.contains("gb-thanks")) {
    flushLead();
  }
  if (document.body && document.body.classList.contains("gb-booking-confirmed")) {
    confirmBooking();
  }
})();
