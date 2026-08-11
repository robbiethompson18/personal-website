---
title: Why It Didn't Work: Browser Agents
date: 2026-08-09
---

Bailey and I spent a little more than a month building better browser agents before pivoting away.
Our initial thesis was:

- clearly people wanted browser agents: Manus was very popular, this was a hot area of research at
  the labs
- we had simple ways to improve on existing techniques (eg giving it better pre-processing of the
  DOM)

## Tech Searching for a Problem

We made a canonical startup mistake: decide what tech you want to build, then figure out who will
use it. In our defense, we had a first customer who trialed our product from almost day one, but ACV
would've been four digits, and there weren't obviously thousands of customers with their same
problem.

## People Wanted Illegal Things

When I did get around to doing more sales, people wanted to use our agents to access websites that
either had a paid API (X, Epic) or very intentionally had no API (LinkedIn). We were on track to get
sued the second we found success.

## No Defensibility

Several customers told us our browser agents were much better than what others offered out of the
box at the time. This was entirely a result of using cute tricks like parsing the accessibility tree
well. It took Anthropic ~4x longer to catch up than I expected. But that was still 10x too little
time to build a durable business.
