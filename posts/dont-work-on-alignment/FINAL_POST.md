---
title: Don't Work on Alignment
date: 2026-08-10
draft: true
---

Epistemic status: this is not an argument that AI risk is fake, or that alignment research doesn't
matter. It's an argument that _you_ (me) joining the queue for alignment jobs is a worse trade than
the alternatives, for reasons that have almost nothing to do with how important alignment is.

Winding down the company is its own post. The question I actually have to answer is what to do with
the next several years, and the default answer from basically everyone in my social graph is: go
work on alignment. I want to write down why that's the wrong default, in enough detail that I can't
talk myself back into it in six months.

## The Reflexive Answer

If you are a technical, safety-pilled twenty-something in SF right now, "alignment" is what
consulting was for Ivy League grads in 2005, or "learn to code" was in 2015. It's the terminal
career move. You don't have to justify it at a dinner party. Nobody asks a follow-up question when
you say you're "working on AI safety." It sounds serious, it pays well, and it comes pre-loaded with
moral permission: you get to build the thing that might end the world, and also be one of the good
guys who was trying to stop it from happening.

Every EA-adjacent person I know uses some version of the importance/neglectedness/tractability
framework to justify their career, and every one of them nails "important" and skips the arithmetic
on "neglected." Alignment clears the importance bar by more than almost anything else you could work
on. That's exactly why it stopped being neglected.

## Neglectedness Has an Expiration Date

In 2022, 80,000 Hours estimated about 300 people worldwide were working on technical approaches to
AI existential risk. By 2025 a survey put the number at 1,100, and 80,000 Hours itself now guesses
the real number, including everyone loosely focused on the most important risks from AGI, is in the
low thousands.[^growth] That's not neglected anymore, that's a field that grew 4-10x in three years.
Compare that growth rate to literally any other cause area you could name. Malaria nets aren't
getting 4x more people working on them every three years. Nothing is, because nothing else has three
trillion dollars of frontier lab valuation and a live shot at the most interesting engineering
problem in human history pulling talent toward it.

The tell is that 80,000 Hours, an organization whose entire existence is to route people into
high-impact careers, published a post in January 2026 called "The most overlooked roles in AI
safety," and the answer wasn't "more alignment researchers." It was operations and management roles,
the unsexy multiplier jobs nobody wants because they don't sound serious at a dinner
party.[^overlooked] When the org that has spent a decade telling smart people to go do alignment
starts publicly correcting course toward "actually we need people who are good at logistics," that's
not a subtle signal. That's them telling you the pipe is full.

## The Flagship Effort Imploded

Here's the part that should worry you more than the headcount numbers: the most famous, best-funded,
most explicitly mission-driven alignment team in the industry got dissolved.

OpenAI's Superalignment team, announced with real fanfare in 2023 and staffed with some of the most
credentialed alignment researchers alive, was disbanded within about a year, shortly after its
co-lead Jan Leike quit and said publicly that safety had "taken a backseat to shiny
products."[^superalignment] The follow-up effort, a "Mission Alignment" team stood up afterward, got
disbanded too, in 2025.

If your plan is "join a lab, be the person who tips a trillion-dollar org toward safety from the
inside," you are making a bet on org-chart stability, not a bet on the problem being important. The
most well-resourced version of that bet, at the lab that invented the strategy, didn't survive
contact with a product roadmap. You should update on that, hard, before you make the same bet with
your own career.

And even where the internal safety function hasn't been disbanded, it's already huge. One estimate
puts Anthropic at around 5,000 employees, with roughly 35% of them in a combined "Research & AI
Safety" bucket.[^anthropicsize] That's something like 1,750 people. If you join that team, you are
not employee number one making the pivotal difference. You are employee number 1,751, and the
marginal value of number 1,751 is not the same number the importance/neglectedness framework spit
out when you first ran it in your head.

## Two Jobs Wearing One Name

Part of the confusion is that "alignment" describes two very different jobs, and the discourse
treats them as one.

Job one is theory: interpretability research, agent foundations, the math of what a value function
even is. This is genuinely talent-constrained, but the talent it wants is a specific kind, closer to
a pure mathematician or a theoretical physicist than a software engineer. If you don't have that
profile, showing up doesn't help much; you'd be competing for a small number of seats against people
who have spent a decade optimizing for exactly this.

Job two is applied engineering: building the sandboxes, harnesses, evaluation pipelines, and
monitoring infrastructure that theory needs in order to be tested against anything real. This job is
not talent-constrained in the same way. It's constrained by people who can actually ship
infrastructure under deadline pressure, which is a much more common skill and one you happen to have
in spades.

The problem is that job two is chronically understaffed relative to job one, because job one is the
prestigious version that gets the conference talks and the Twitter followers, and job two is the
"ops" work that 80,000 Hours just admitted nobody wants to do. If you go looking for "alignment
jobs" you'll mostly find postings that assume you're candidate one. The places that actually need
candidate two are a level removed from the word "alignment" entirely.

## Where the Bodies Aren't

So: not alignment, but not "do something unrelated to AI" either. Here's where I think the actual
gap is, ranked by how much I think your specific skills matter there.

**AI control and evals infrastructure.** Control is the part of the safety portfolio that assumes
models might already be misaligned and asks what systems keep that safe anyway, which is a much more
concrete engineering problem than alignment theory. METR, Redwood Research, and Apollo Research all
work in this space, and all of them are small: Redwood was at 12 full-time staff in early 2026,
after shrinking to four in 2023 before growing back.[^redwood] These are not thousand-person orgs
where you're a rounding error. Apollo has also shifted its research agenda from scheming evals
toward a broader "Science of Scheming" program and is running hiring rounds through the back half
of 2026.[^apollo] This is, functionally, building sandboxed environments where an agent tries to get
away with something and you build the harness that catches it. That is an almost exact description
of what browser agents and OpenClaw hosting already forced me to learn: how agents actually fail,
what they try when the obvious path is blocked, how to instrument a system you don't fully trust.

**AI security, specifically model weight security.** This barely gets discussed under the
"alignment" banner at all, which is exactly the point. A 2024 RAND report on securing AI model
weights laid out, in detail, how far frontier labs are from being able to stop a serious
nation-state actor from stealing their weights.[^weights] Anthropic's own CISO has said publicly
that "defenders are behind." Model welfare gets a research program and a conference. Weight
security, arguably the more legible and more urgent problem, gets a report nobody outside the field
read. This is straightforwardly an infra and security-engineering problem, not a philosophy problem,
and it's the single closest match to "guy who built and ran hosting infrastructure for autonomous
agents" that exists in this entire space.

**AI-enabled biosecurity.** SecureBio and its Nucleic Acid Observatory project run the biosecurity
evaluations that get cited directly in the model cards of OpenAI, Anthropic, and Google, meaning a
small nonprofit is already load-bearing for how the biggest labs assess their own most catastrophic
misuse risk.[^securebio] They currently have about a dozen open roles, including a software engineer
position explicitly for scaling those evaluations. This is a field where the ratio of "leverage over
what frontier labs actually do" to "number of people doing it" is absurd, and most of the roles want
engineers, not virologists.

**Governance, especially compute governance.** This one comes with a warning label. In 2025 the US
AI Safety Institute was renamed the Center for AI Standards and Innovation, with "safety" explicitly
removed from both the name and the mission, reoriented toward national security testing and
international competitiveness instead.[^caisi] That's not proof governance work doesn't matter, it's
proof governance is genuinely contested terrain, the kind of place where showing up matters because
the default outcome if good people don't show up is that the mission gets quietly redefined out from
under you. Epoch AI does the empirical work (compute trends, timelines, who actually has how many
chips) that everyone else's governance arguments depend on and rarely credit. The Institute for AI
Policy and Strategy does the harder, more contested work of turning that data into actual policy
proposals.[^governance] Neither field pays as well as a lab job. Both are short on people who can
write code and read a paper in the same afternoon, which describes you.

**Model welfare, if you want to be early to something genuinely strange.** Eleos AI is a handful of
people, funded partly by Anthropic itself, and their research already shaped the formal welfare
assessments included in Claude Opus 4.6's system card in February 2026.[^eleos] I don't know if this
field is right, and neither does anyone else, which is exactly why it counts as neglected. This is
not a top recommendation. It's the option for someone who'd rather be early and wrong than late and
safe.

**Post-AGI economic and institutional design.** The one I have the least concrete advice for,
because there's barely an "org" version of this to point you at yet. I already wrote about the shape
of the problem: if AI automates everything valuable, we still need somewhere for humans to put their
need for structure and responsibility, and almost nobody is doing serious work on what that looks
like institutionally rather than as a blog post.[^bullshit] This is closer to something you'd have
to build than something you'd apply to. Mentioning it because the gap is real, not because I have a
hiring link for you.

## Why This Is About You Specifically

None of the above is a general argument that everyone should avoid alignment and pile into control
or biosecurity instead; that would just relocate the crowding problem five years from now. It's an
argument about fit.

I spent the last stretch of my career building browser agents and hosting infrastructure for other
people's agents. Both companies failed commercially, but neither failure was about the technical
work. I know what it looks like when an autonomous agent finds the seam in a system nobody thought
to guard. I know how to stand up infrastructure fast, under real deadline pressure, for workloads
nobody has run before. I know, from the inside, what "AI productivity psychosis" looks like when a
hundred founders convince themselves a landing page and an agent equal a business.[^psychosis] None
of that is theory chops. All of it maps directly onto control, evals infrastructure, and security
work, and none of it maps especially well onto interpretability research or agent foundations math.

Going to work on alignment, for me, would mean taking a skill set that's unusually well suited to a
handful of small, understaffed, high-leverage orgs, and instead pointing it at the most crowded,
highest-status, most internally unstable corner of the field, because that's the corner with the
best name recognition. That's not a safety-maximizing decision. It's a status-maximizing decision
wearing a safety costume, and I'd rather notice that now than in three years.

## What I'm Actually Going to Do

Apply to the infra and engineering roles at METR, Redwood Research, and Apollo Research before
anything with "alignment" in the title. Look seriously at security roles, not research roles, at the
labs and at RAND. Talk to SecureBio about what a software engineer scaling their biosecurity
evaluations actually does day to day. Skip the governance track unless I find a concrete project,
not a vibe. Deprioritize model welfare, not because it's silly, but because it isn't where my skills
are leveraged.

And the general version, for anyone reading this who isn't me: check the neglectedness term before
you join the queue. The field that gets talked about most at parties is, almost definitionally, not
the one that needs you most.

[^growth]:
    [AI safety technical research | Career review | 80,000 Hours](https://80000hours.org/career-reviews/ai-safety-technical-research/)
    on the 2022 estimate of roughly 300 people and the 2025 survey putting the number closer to
    1,100, plus
    [The most overlooked roles in AI safety, Jan 2026](https://80000hours.org/2026/01/the-most-overlooked-roles-in-ai-safety/)
    on where 80,000 Hours now sees the actual gap.

[^overlooked]:
    [The most overlooked roles in AI safety | 80,000 Hours](https://80000hours.org/2026/01/the-most-overlooked-roles-in-ai-safety/)

[^superalignment]:
    OpenAI's Superalignment team was announced in 2023 and dissolved in 2024, shortly after co-lead
    Jan Leike's departure and public criticism that safety work had lost resources to product
    launches. A successor "Mission Alignment" team was disbanded in 2025.

[^anthropicsize]:
    [How Many Employees Does Anthropic Have in 2026? (~5,000)](https://jobsbyculture.com/blog/anthropic-employee-count-2026),
    citing an internal breakdown of roughly 35% Research & AI Safety, 30% Engineering, 15%
    Go-to-Market & Sales, 10% Policy & Communications, 10% Operations/HR/Finance.

[^redwood]:
    [Redwood Research](https://www.redwoodresearch.org/) and
    [Redwood Research | Organizations | Longterm Wiki](https://www.longtermwiki.com/organizations/redwood-research),
    on staff shrinking to four full-time in early 2023 and growing back to roughly 12 by early 2026.

[^apollo]:
    [Apollo Update May 2026 – Apollo Research](https://www.apolloresearch.ai/blog/apollo-update-may-2026/)

[^weights]:
    [Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models | RAND (2024)](https://www.rand.org/pubs/research_reports/RRA2849-1.html),
    and
    [Defenders Are Behind: Anthropic's CISO on AI Security, Claude, and Protecting Model Weights](https://guruchahal.substack.com/p/defenders-are-behind-anthropics-ciso).

[^securebio]:
    [Software Engineer, AI Safety and Biosecurity – SecureBio](https://securebio.org/careers/software-engineer-ai-safety-and-biosecurity/)
    and [Job board | 80,000 Hours - SecureBio](https://jobs.80000hours.org/organisations/securebio).

[^caisi]:
    [Trump administration rebrands AI Safety Institute | FedScoop](https://fedscoop.com/trump-administration-rebrands-ai-safety-institute-aisi-caisi/),
    on the June 2025 renaming of the US AI Safety Institute to the Center for AI Standards and
    Innovation, with "safety" dropped from the name and the mission reoriented toward national
    security testing and international standards competition.

[^governance]:
    [Epoch AI](https://epoch.ai/) and [Institute for AI Policy and Strategy](https://www.iaps.ai/),
    on compute forecasting and policy research respectively.

[^eleos]:
    [Eleos commends Anthropic model welfare efforts | Eleos AI](https://eleosai.org/post/eleos-commends-anthropic-model-welfare-efforts/),
    on Kyle Fish's role as Anthropic's first dedicated model welfare researcher, engaged through
    Eleos AI, and the formal welfare assessments included in the Claude Opus 4.6 system card in
    February 2026.

[^bullshit]:
    I wrote about this at more length in
    [A Bullshit Job For Every American](/blog/a-bullshit-job-for-every-american/).

[^psychosis]:
    See [Thoughts on AI: March 2026](/blog/thoughts-on-ai-march-2026/) and
    [Why It Didn't Work: OpenClaw Hosting](/blog/why-it-didnt-work-openclaw-hosting/).
