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
    // The footnote is already on screen in the margin (sidenotes, below); cites still pop up.
    if (document.body.classList.contains("has-sidenotes") && ref.closest(".footnote-ref")) return;
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

// Sidenotes (LessWrong/Tufte style): on a wide screen every footnote's text also
// sits in the right margin, level with the line that cites it, so you read it
// without hovering. The Notes list at the bottom stays for narrow screens, no-JS
// and RSS. Below the breakpoint the margin is too thin, so the hover popup above
// takes over again.
(function () {
  const main = document.querySelector("main.post");
  if (!main) return;
  // Markers inside the Notes list itself (a footnote citing a footnote) get no sidenote.
  const refs = [...main.querySelectorAll(".footnote-ref a")].filter((a) => !a.closest(".footnotes"));
  if (!refs.length) return;

  // Must match the `.has-sidenotes` breakpoint reasoning in blog.css: a 45rem column
  // plus a 15.5rem note on each side's worth of margin.
  const wide = matchMedia("(min-width: 80rem)");

  // One sidenote per footnote, placed at its first marker. A reused footnote's later
  // markers just highlight that same note.
  const notes = new Map(); // "#fn1" -> { note, refs: [a, ...] }
  for (const ref of refs) {
    const href = ref.getAttribute("href");
    if (notes.has(href)) {
      notes.get(href).refs.push(ref);
      continue;
    }
    const target = document.getElementById(href.slice(1));
    if (!target) continue;
    const note = document.createElement("aside");
    note.className = "sidenote";
    const num = ref.textContent.replace(/[[\]]/g, ""); // "[3]" -> "3"
    note.innerHTML = `<span class="sidenote-num">${num}</span>${target.innerHTML}`;
    main.appendChild(note);
    notes.set(href, { note, refs: [ref] });
  }

  function layout() {
    const on = wide.matches;
    document.body.classList.toggle("has-sidenotes", on);
    if (!on) return;
    const mainTop = main.getBoundingClientRect().top;
    const clampPx = window.innerHeight / 3; // must match max-height: 33.33vh in blog.css
    let floor = -Infinity; // bottom of the last placed note: stack, never overlap
    for (const { note, refs } of notes.values()) {
      // A marker inside a closed <details class="aside"> has no boxes; hide its note
      // until the aside opens (the ResizeObserver re-runs this on toggle).
      if (!refs[0].getClientRects().length) {
        note.classList.add("off");
        continue;
      }
      note.classList.remove("off");
      const top = Math.max(refs[0].getBoundingClientRect().top - mainTop, floor);
      note.style.top = `${top}px`;
      // A long note is cut to a third of the window (fade + expand on hover, see
      // blog.css) so it doesn't shove every later note far below its marker. The 1.2x
      // slack means we never hide just a line or two. scrollHeight is the full height
      // even while clamped, so this is stable across re-layouts.
      const clamped = note.scrollHeight > clampPx * 1.2;
      note.classList.toggle("clamped", clamped);
      floor = top + (clamped ? clampPx : note.scrollHeight) + 12;
    }
  }

  // Images, fonts, KaTeX and opening asides all move markers after first paint.
  // The notes are absolutely positioned, so they never resize main: no feedback loop.
  // The window resize catches height-only changes, which move the clamp but not main.
  new ResizeObserver(layout).observe(main);
  window.addEventListener("resize", layout);
  wide.addEventListener("change", layout);
  layout();

  // Hovering a marker lights up its note, and vice versa. Clicking a marker while the
  // note is beside it would only yank you to the bottom, so flash the note instead.
  for (const { note, refs } of notes.values()) {
    const on = () => {
      note.classList.add("active");
      refs.forEach((r) => r.classList.add("active"));
    };
    const off = () => {
      note.classList.remove("active");
      refs.forEach((r) => r.classList.remove("active"));
    };
    [note, ...refs].forEach((el) => {
      el.addEventListener("mouseenter", on);
      el.addEventListener("mouseleave", off);
    });
    refs.forEach((r) =>
      r.addEventListener("click", (e) => {
        if (!document.body.classList.contains("has-sidenotes") || note.classList.contains("off")) return;
        e.preventDefault();
        note.classList.remove("flash");
        void note.offsetWidth; // restart the animation on repeat clicks
        note.classList.add("flash");
      }),
    );
  }
})();

// Keep footnote round trips out of the Back button. Clicking a marker jumps to its
// note and adds a history entry, so Back returns you to your spot (the standard,
// and what phone readers expect). But ↩︎ is also a jump, so without this every
// note read cost two entries and Back replayed them all before leaving the page.
// If you reached a note by clicking its marker, ↩︎ now *is* Back: the pair nets to
// zero entries and the browser restores your exact scroll position. Arriving any
// other way (a shared #fn3 link) leaves ↩︎ as a plain jump. Cites work the same.
(function () {
  let arrivedAt = null; // the hash a marker click just took us to
  // Registered after the sidenote handler, which preventDefaults on wide screens:
  // no jump there, so nothing to undo.
  document.querySelectorAll(".footnote-ref a, a.cite").forEach((ref) =>
    ref.addEventListener("click", (e) => {
      if (!e.defaultPrevented) arrivedAt = ref.getAttribute("href");
    }),
  );
  document.querySelectorAll(".footnote-backref, .cite-backref").forEach((back) =>
    back.addEventListener("click", (e) => {
      const item = back.closest("[id]"); // the <li id="fn3"> / source item holding this ↩︎
      if (!item || arrivedAt !== `#${item.id}` || location.hash !== arrivedAt) return;
      e.preventDefault();
      arrivedAt = null;
      history.back();
    }),
  );
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
