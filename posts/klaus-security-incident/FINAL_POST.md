---
title: Klaus Security Incidents
date: 2026-09-14
rating: 1
---

In early April Klaus had a string of malicious users sign up for our service.

## Unprotected Endpoints

Late on the night of April 6, I noticed that we sent a welcome email to bughunter@gmail.com.[^ne] I
quickly checked the logs and noticed anomalous activity from several new accounts.

[^ne]: Stylized, not exactly this email.

They found one bug: an unprotected organization creation endpoint. The attackers used this to create
an additional VM and claim extra token credits.

The bug was fixed three hours after discovery. I added Express middleware in front of all of
BetterAuth endpoints and made them off by default.

I suspect these users were pen-testers.

## Free Trial Fraud

On April 2 we implemented a 2 day free trial and quickly saw lots of fraud:

- Users created fake accounts to claim a referral credit. We patched by only crediting referrers on
  first payment of the referee.
- Spammers used fake credit cards to create new accounts for free token credits.
- Many accounts were made with discount codes we had never made public.

We used the following mitigations to deter scammers:

- Reported accounts made on the same credit card with clear burner emails to Stripe.
- Rate-limited our discount code endpoint.
- Captured client IP at signup, then flagged any new signup sharing an IP with a banned account.
- Stored the Stripe card fingerprint on each org to catch the same card across accounts.
- Created alerts for high-volume referrers and referral chains through banned accounts.

In total we found 156 fraudulent accounts. Average time to deactivation was 289 minutes. In total
spammers were able to spend $314 in token credits of the ~$10,000 they were granted.

Eventually we decided that we were spending too much time combating spammers, and we eliminated our
free trial.
