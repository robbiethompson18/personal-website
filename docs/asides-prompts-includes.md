# Asides, verbatim prompts, and includes

How the three pieces added 2026-09-01 fit together, and the ways they bite. Read before adding a
collapsible box, pasting an eval prompt or transcript into a post, or splitting a long excerpt out
of `FINAL_POST.md`.

## Aside: a collapsible tangent box

Native `<details>` in the markdown; `html: true` in markdown-it passes it through.

```markdown
<details class="aside">
<summary>Why this doesn't generalize</summary>

Any markdown: paragraphs, cites, footnotes, math, fences, includes.

</details>
```

- **The blank line after `</summary>` is load-bearing.** markdown-it treats `<details>` as an HTML
  block that runs until the first blank line. Without the blank line, the body is emitted as raw
  HTML and none of the markdown inside renders.
- Styling is `details.aside` in `blog.css`, tinted from `--aside` (saturated violet) mixed into
  `--bg`. The triangle and the "expand / collapse" hint are `summary::before` / `::after`; the hint
  hides on touch devices.
- The whole box toggles, not just the summary line. That is the last IIFE in `footnotes.js`: it
  flips `open` on click unless the click landed on a link or the summary (the browser handles those)
  or the user was selecting text. No JS still works, you just have to click the label.
- Closed by default; add `open` to the tag to render one expanded.
- The RSS feed carries the `<details>` markup as-is. Substack strips it and shows the body inline.

## Verbatim text: the `prompt` fence

An eval prompt or transcript is plain text with meaningful line breaks. Rendering it as markdown
mangles it, and Prettier mangles it a second time. What actually happens to bare pasted text:

- markdown-it collapses single newlines to spaces, so `A. 0 / B. 1 / C. 2` become one line.
- `### Heading` becomes a real `<h3>` with an id and a hover `#` anchor.
- `<!-- comments -->` disappear. `<uploaded_files>`-style tags render as nothing.
- Lines indented four spaces (a traceback) become code blocks.
- Prettier's `proseWrap: always` then rewraps the source to 100 columns. That is a permanent edit to
  the file, not a rendering glitch.

The only container both tools leave alone is a fenced code block. Tag it `prompt`:

````markdown
```prompt
The following are multiple choice questions...
```
````

`blog.css` renders `pre:has(> code.language-prompt)` as wrapped text in the reading font with line
breaks preserved and no code box. Change the font-family on that rule to get wrapped monospace
instead. Use a longer fence (four or more backticks) when the content contains triple backticks.

If the pasted text really is markdown (a GitHub issue body, say) and you want it rendered that way,
that is a different choice: paste it as ordinary markdown between `<!-- prettier-ignore-start -->`
and `<!-- prettier-ignore-end -->`. You still lose the HTML comments and gain heading anchors, but
images and inline code render. `posts/extending-evaluation-awareness/excerpts/swe-bench.md` does
both: fenced scaffolding, then the issue as markdown.

## Includes: keep the excerpt out of the post

```markdown
<!-- include excerpts/swe-bench.md -->
```

On its own line, replaced with the file's contents (path relative to the post folder) by
`expandIncludes` in `build.js`, just before `md.render`.

- Keep the `.md` extension. The builder only renders `FINAL_POST.md` and only copies non-`.md` files
  to `blog/`, so an `.md` excerpt is neither published as a page nor copied. `copyAssets` removes
  the resulting empty `excerpts/` output dir.
- `lint.sh` formats every `**/*.md`, excerpts included. Fenced content is safe; markdown content
  needs the prettier-ignore range.
- **Every code fence inside a prettier-ignore range must be closed.** An excerpt cut mid-code-block
  leaves the fence open, the `<!-- prettier-ignore-end -->` marker gets swallowed into it, the range
  never forms, and Prettier reflows everything. This happened once; it looked like the ignore
  markers "didn't work".
- Expansion runs after `checkContent`, on purpose: the footnote, cite, and math checks are for
  Robbie's prose and would otherwise trip on stray `$` in someone else's benchmark. They do not look
  inside includes.
- A missing include file throws from `readFileSync` and fails the build.

## Asset cache-busting (why a CSS edit used to look broken)

The dev server (`python -m http.server`) sends no cache headers, so Chrome kept an old `blog.css`
for the session; the aside border showed but a rule added ten minutes later did not. `build.js` now
content-hashes `blog.css` and `footnotes.js` into their URLs (`/blog.css?v=76ed054e`), and the dev
watcher rebuilds when either file changes. Restart `prd` after changing `package.json` for the new
watch paths to apply.
