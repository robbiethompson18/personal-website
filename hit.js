// First-party page-view counter and like button. The site's Worker does the counting
// (worker/api.js). No cookies; nothing is read back, so no counts are ever shown.
(() => {
  // Only the real site counts: local dev, the .dev/ build and the workers.dev URL don't.
  const live = location.hostname === "robbiewmthompson.com";
  const path = location.pathname;

  // sendBeacon is queued by the browser, so it still goes out if the page is closed or
  // navigated away from right after. Failures are ignored: analytics must never break a page.
  function send(endpoint, body) {
    if (!live) return;
    const json = JSON.stringify(body);
    if (navigator.sendBeacon?.(endpoint, json)) return;
    fetch(endpoint, { method: "POST", body: json, keepalive: true }).catch(() => {});
  }

  // Only the referring hostname leaves the browser, never the full URL.
  send("/api/hit", { path, referrer: document.referrer && new URL(document.referrer).hostname });

  // Post pages end with a like button (build.js). Like only, no unlike: localStorage is
  // what remembers it, so the heart stays filled and this browser can't like twice.
  const like = document.querySelector(".like");
  if (!like) return;
  const key = `liked:${path}`;
  let liked = false;
  try {
    liked = !!localStorage.getItem(key);
  } catch {} // storage can be blocked; the button then just starts empty
  if (liked) like.setAttribute("aria-pressed", "true");
  like.addEventListener("click", () => {
    if (liked) return;
    liked = true;
    like.setAttribute("aria-pressed", "true");
    try {
      localStorage.setItem(key, "1");
    } catch {}
    send("/api/like", { path });
  });
})();
