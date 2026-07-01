// Progressive enhancement for footnotes.
//
// Without JS: footnote markers are plain anchor links that jump to the
// definitions at the bottom of the article, and the back-arrow returns you.
// With JS (desktop): hovering a marker shows the footnote text in a popup so
// you never lose your place. On touch devices there's no hover, so tapping
// still just jumps to the bottom — which is the right behavior there anyway.

(function () {
  const refs = document.querySelectorAll(".footnote-ref a");
  if (!refs.length) return;

  const tip = document.createElement("div");
  tip.className = "fn-tooltip";
  document.body.appendChild(tip);

  let hideTimer = null;

  function show(ref) {
    clearTimeout(hideTimer);
    const id = ref.getAttribute("href").slice(1); // "#fn1" -> "fn1"
    const target = document.getElementById(id);
    if (!target) return;

    tip.innerHTML = target.innerHTML;
    tip.classList.add("visible");

    // Position above the marker, clamped to the viewport, accounting for scroll.
    const r = ref.getBoundingClientRect();
    const tr = tip.getBoundingClientRect();
    const margin = 8;
    let left = window.scrollX + r.left + r.width / 2 - tr.width / 2;
    left = Math.max(margin, Math.min(left, window.scrollX + window.innerWidth - tr.width - margin));

    let top = window.scrollY + r.top - tr.height - margin;
    if (r.top - tr.height - margin < 0) top = window.scrollY + r.bottom + margin; // flip below if no room above

    tip.style.left = `${left}px`;
    tip.style.top = `${top}px`;
  }

  function hide() {
    hideTimer = setTimeout(() => tip.classList.remove("visible"), 80);
  }

  refs.forEach((ref) => {
    ref.addEventListener("mouseenter", () => show(ref));
    ref.addEventListener("mouseleave", hide);
  });
  tip.addEventListener("mouseenter", () => clearTimeout(hideTimer));
  tip.addEventListener("mouseleave", hide);
})();

// Click a heading's "#" to copy a direct link to that section (Substack-style).
// Own IIFE so it still runs on posts that have no footnotes.
(function () {
  const anchors = document.querySelectorAll(".heading-anchor");
  if (!anchors.length) return;

  anchors.forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const hash = a.getAttribute("href"); // "#some-slug"
      const url = location.origin + location.pathname + hash;
      history.replaceState(null, "", hash); // update the URL bar without a scroll jump
      navigator.clipboard?.writeText(url);
      a.textContent = "✓"; // brief confirmation; mouse is still over the heading so it stays visible
      setTimeout(() => (a.textContent = "#"), 1000);
    });
  });
})();
