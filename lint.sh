#!/bin/bash
# Format the landing-page HTML and every Markdown file in the repo with Prettier.
# proseWrap:always (.prettierrc) reflows markdown prose + lists to printWidth, so
# don't hand-wrap markdown — write long lines and let this rewrap them.
# node_modules/.git are auto-ignored by Prettier.
# First move each post's footnote definitions under the paragraph that cites them, and its
# `{@id}:` sources to the end of the file (place-notes.js). Before Prettier, which then
# rewraps whatever moved.
node place-notes.js
npx prettier --write "*.html" "**/*.md"
