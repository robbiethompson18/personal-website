#!/bin/bash
# Format the landing-page HTML and every Markdown file in the repo with Prettier.
# proseWrap:always (.prettierrc) reflows markdown prose + lists to printWidth, so
# don't hand-wrap markdown — write long lines and let this rewrap them.
# node_modules/.git are auto-ignored by Prettier.
npx prettier --write "*.html" "**/*.md"
