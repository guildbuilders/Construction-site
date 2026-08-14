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
   in the web container's Google tag and the Custom Loader path in Stape. */
const TAGGING_PATH = "/metrics";

const TAGGING_HOST = "REPLACE_WITH_STAPE_TAGGING_HOST";

/* Set to null once TAGGING_HOST is a custom subdomain. Stape only needs this
   header to disambiguate traffic arriving at a shared stape.io host. */
const STAPE_HOST = "guildbuildersgroup.com";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

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
