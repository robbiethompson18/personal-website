// Progressive enhancement for footnotes.
//
// Without JS: footnote markers are plain anchor links that jump to the
// definitions at the bottom of the article, and the back-arrow returns you.
// With JS (desktop): hovering a marker shows the footnote text in a popup so
// you never lose your place. On touch devices there's no hover, so tapping
// still just jumps to the bottom — which is the right behavior there anyway.

(function () {
  // Both aside markers (.footnote-ref a -> #fnN) and source-cite phrases
  // (a.cite -> #src-id) preview their target text on hover.
  const refs = document.querySelectorAll(".footnote-ref a, a.cite");
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

    // Flip below the marker when there's no room above; the CSS bridge follows.
    const flipBelow = r.top - tr.height - margin < 0;
    const top = flipBelow ? window.scrollY + r.bottom + margin : window.scrollY + r.top - tr.height - margin;
    tip.classList.toggle("below", flipBelow);

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

  // navigator.clipboard is unavailable on plain http (non-localhost) and can
  // silently reject even where present, so fall back to the execCommand hack.
  function copy(text) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).catch(legacyCopy);
    } else {
      legacyCopy();
    }
    function legacyCopy() {
      const el = document.createElement("textarea");
      el.value = text;
      el.style.position = "fixed";
      el.style.opacity = "0";
      document.body.appendChild(el);
      el.select();
      try {
        document.execCommand("copy");
      } catch {}
      document.body.removeChild(el);
    }
  }

  anchors.forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const hash = a.getAttribute("href"); // "#some-slug"
      const url = location.origin + location.pathname + hash;
      history.replaceState(null, "", hash); // update the URL bar without a scroll jump
      copy(url);
      a.textContent = "✓"; // brief confirmation; mouse is still over the heading so it stays visible
      setTimeout(() => (a.textContent = "#"), 1000);
    });
  });
})();

// Asides (<details class="aside">): make the whole box toggle, not just the
// <summary> line. Native <details> still owns the state, so no-JS works too.
// Skip when the click lands on a link (navigate), on the summary itself (the
// browser already toggles it), or when the user was selecting text.
(function () {
  document.querySelectorAll("details.aside").forEach((box) => {
    box.addEventListener("click", (e) => {
      if (e.target.closest("a, summary")) return;
      if (window.getSelection()?.toString()) return;
      box.open = !box.open;
    });
  });
})();
