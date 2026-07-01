#!/bin/bash
# Format the landing-page HTML and every Markdown file in the repo with Prettier.
# proseWrap:always (.prettierrc) reflows markdown prose + lists to printWidth, so
# don't hand-wrap markdown — write long lines and let this rewrap them.
# node_modules/.git are auto-ignored by Prettier; POST_DRAFT.md / POST_RESEARCH.md
# are skipped via .prettierignore.
npx prettier --write "*.html" "**/*.md"
