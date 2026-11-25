// First-party page-view counter and like button. The site's Worker does the counting
// (worker/api.js). No cookies; nothing is read back, so no real counts are ever shown
// (the like count beside each heart is a gag, see fakeCount).
(() => {
  // Only the real site counts: local dev and the .dev/ build don't.
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

  // Post pages have two like buttons (build.js): beside the title and at the end of
  // the text. Like only, no unlike: localStorage is what remembers it, so the hearts
  // stay filled and this browser can't like twice.
  const likes = document.querySelectorAll(".like");

  // A gag like count beside each heart, rolled fresh on every page load and unrelated
  // to the real likes (which are never read back). Half the time a plausible four-digit
  // number, half the time something silly. Liking adds one to the four-digit number and
  // leaves the silly ones alone.
  const SILLY = [
    "sooo many",
    "BB(6)",
    "3↑↑↑3",
    "TREE(3)",
    "g₆₄", // Graham's number
    "SSCG(3)",
    "Rayo(10¹⁰⁰)",
    "a googolplex",
    "2¹³⁶²⁷⁹⁸⁴¹ − 1", // largest known prime (2024)
    "52!",
    "1 mol",
    "ℵ₀",
    "∞",
    "NaN",
    "−4",
    "i",
  ];
  const pick = (n) => Math.floor(Math.random() * n);
  function fakeCount() {
    if (Math.random() < 0.5) return 1000 + pick(9000);
    // a third of the silly ones are random scientific notation, e.g. 4e57
    if (Math.random() < 1 / 3) return `${1 + pick(9)}e${5 + pick(96)}`;
    return SILLY[pick(SILLY.length)];
  }
  let count = fakeCount();
  const counts = [...likes].map((like) => {
    const span = document.createElement("span");
    span.className = "like-count";
    like.after(span);
    return span;
  });
  const showCount = () => counts.forEach((span) => (span.textContent = count));
  showCount();
  const key = `liked:${path}`;
  let liked = false;
  try {
    liked = !!localStorage.getItem(key);
  } catch {} // storage can be blocked; the buttons then just start empty
  const fill = () => likes.forEach((like) => like.setAttribute("aria-pressed", "true"));
  if (liked) fill();
  likes.forEach((like) =>
    like.addEventListener("click", () => {
      if (liked) return;
      liked = true;
      fill();
      if (typeof count === "number") {
        count += 1;
        showCount();
      }
      try {
        localStorage.setItem(key, "1");
      } catch {}
      send("/api/like", { path });
    }),
  );
})();
