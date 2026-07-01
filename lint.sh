#!/bin/bash
# Format the landing-page HTML and each post's Markdown with Prettier.
# proseWrap:always (.prettierrc) reflows markdown prose + lists to printWidth, so
# don't hand-wrap markdown — write long lines and let this rewrap them.
# POST_DRAFT.md / POST_RESEARCH.md are skipped via .prettierignore.
npx prettier --write "*.html" "posts/**/*.md"
