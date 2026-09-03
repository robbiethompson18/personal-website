// markdown-it plugin: source citations, a second footnote-like stream that is
// visually distinct from the aside/commentary footnotes markdown-it-footnote
// handles.
//
// Authoring:
//   Producing a steak takes ~[1,590 sq ft of land](@steak).   <- reference
//   {@steak}: Poore & Nemecek (2018), *Science*. <https://…>  <- definition
//
// A reference is just a normal markdown link whose href is `@id` — so both
// markdown-it and Prettier already understand the structure, and the *phrase*
// (not a superscript number) becomes the clickable anchor. The rendered phrase
// gets a faint-purple underline (`.cite`) and jumps to a "Sources" section that
// this plugin appends after the footnotes, mirroring the footnote tail.
//
// Definitions collect from `{@id}:` lines. `{…}` (not `[…]`) is deliberate:
// `[id]: url` is link-reference-definition syntax that Prettier owns and will
// rewrite or drop, whereas `{@id}:` is plain text to Prettier. A definition may
// wrap across lines (Prettier reflows prose to 100 cols); we join until a blank
// line or the next definition.

export default function cite(md) {
  // --- block: collect `{@id}: source text` definitions, emit nothing ------
  md.block.ruler.before("reference", "cite_definition", (state, startLine, endLine, silent) => {
    const start = state.bMarks[startLine] + state.tShift[startLine];
    const firstLine = state.src.slice(start, state.eMarks[startLine]);
    const m = /^\{@([\w-]+)\}:\s*(.*)$/.exec(firstLine);
    if (!m) return false;
    if (silent) return true;

    let content = m[2];
    let next = startLine + 1;
    for (; next < endLine; next++) {
      const s = state.bMarks[next] + state.tShift[next];
      const e = state.eMarks[next];
      if (s >= e) break; // blank line ends the definition
      const line = state.src.slice(s, e);
      if (/^\{@[\w-]+\}:/.test(line)) break; // next definition
      content += " " + line.trim();
    }

    const env = (state.env.cites ??= { defs: {}, order: [] });
    env.defs[m[1]] = content.trim();
    state.line = next;
    return true;
  });

  // --- inline refs: rewrite `[phrase](@id)` links into citation anchors ---
  md.core.ruler.after("inline", "cite_refs", (state) => {
    const env = (state.env.cites ??= { defs: {}, order: [] });
    for (const blockTok of state.tokens) {
      if (blockTok.type !== "inline") continue;
      for (const tok of blockTok.children) {
        if (tok.type !== "link_open") continue;
        const href = tok.attrGet("href");
        if (!href || !href.startsWith("@")) continue;
        const id = href.slice(1);
        const first = !env.order.includes(id);
        if (first) env.order.push(id);
        tok.attrSet("href", `#src-${id}`);
        tok.attrJoin("class", "cite");
        if (first) tok.attrSet("id", `citeref-${id}`); // back-ref target
      }
    }
  });

  // --- tail: append the Sources section after the footnotes ---------------
  md.core.ruler.push("cite_tail", (state) => {
    const env = state.env.cites;
    if (!env || !env.order.length) return;

    let html =
      '<hr class="sources-sep">\n<section class="sources">\n' +
      '<h2 class="sources-title" id="sources">Sources <a class="heading-anchor" href="#sources" aria-label="Link to this section">#</a></h2>\n' +
      '<p class="sources-note">Claude found these sources. Robbie did not necessarily review them.</p>\n' +
      '<ol class="sources-list">\n';
    for (const id of env.order) {
      const raw = env.defs[id];
      // Fresh env: renderInline re-runs the core ruler (incl. this cite_tail),
      // so reusing state.env — whose cites.order is populated — would recurse.
      const body = raw ? state.md.renderInline(raw, {}) : `<em>missing source: ${id}</em>`;
      html +=
        `<li id="src-${id}" class="source-item">${body}` +
        ` <a href="#citeref-${id}" class="cite-backref" aria-label="Back to text">↩︎</a></li>\n`;
    }
    html += "</ol>\n</section>\n";

    const token = new state.Token("html_block", "", 0);
    token.content = html;
    state.tokens.push(token);
  });
}
