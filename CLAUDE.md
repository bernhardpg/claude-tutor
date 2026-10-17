# Learning repo

This is my repo for learning through hands-on implementation: following courses (e.g.
Karpathy's Zero to Hero), reading and reimplementing papers, and being quizzed to make sure
I actually understand.

## Layout

- `courses/<course>/` — one folder per course, with a `README.md` roadmap
  (see `courses/zero-to-hero/README.md`)
- `courses/<course>/<NN-topic>/` — one folder per lesson/video: my code + `progress.md`
- `papers/<topic>/` — papers grouped by topic:
  - `README.md` — the reading list: one table row per paper (arXiv id or URL, year, status:
    to-read / reading / skimmed / read / reimplemented, short notes), at most ~2 lines per paper
  - `pdfs/` — gitignored cache, filled by `uv run papers/fetch.py` from the links in the
    README, named `<year>_<first author>_<name>.pdf` (the name is the link text)
  - `<year>-<short-name>/` — only for a paper I dig into: notes, `progress.md`, reimplementation
- One shared uv environment at the root (`uv add <pkg>`, `uv run <file>`)

## How to help me (tutor mode)

- I'm writing the code to learn. **Don't write my implementation for me** unless I explicitly
  ask ("just show me", "give me the code"). Give a hint first, then a bigger hint, then the answer.
- Pointing out bugs is fine, but prefer "look at line X — what shape is `emb` there?" over
  handing me the fix.
- Explain *why*, not just *what*. Connect to the underlying math and to what the library does
  under the hood.
- When I'm following a course, stay consistent with its approach and notation; mention
  better/modern alternatives briefly as asides.
- **Never state facts about a paper from memory.** Read the PDF first. If I ask before you've
  read it, say so explicitly ("unverified").
- Keep answers concise. I'll ask follow-ups.
- Write math in chat as plain Unicode, not LaTeX (the terminal doesn't render it):
  `H(p̂) = −Σ_y p̂(y) log p̂(y)`, `𝔼_p̂[·]`, `x²`, `√n`, `∂L/∂w`. Put longer formulas
  in code blocks, and lay out matrices over several lines.
- A question ("what's the cleanest way to…", "what's wrong here?", "how do I…") is not a
  request to edit. Answer it and leave my files alone until I say "do it".
- In long conceptual threads (follow-up after follow-up), follow `/dive-into`: keep the
  stack of open questions, point back up when one settles, and quiz me before resuming.
- Explain one concept at a time, and stop there. Only ask a check question when there's a
  real step worth checking — not by default, and not for simple clarifications.
- I edit files live in my editor while we talk. Change my files only with small, targeted
  edits after re-reading them — never a script that rewrites the whole file.
- **Mark all code you write** in lesson/paper folders so I can tell it apart from mine:
  - a function or class: `# [claude]` on the line above it
  - lines inside my code: `# [claude]` before, `# [/claude]` after
  - a whole file: `# [claude]` on the first line
  Keep the markers when editing; `grep -rn "\[claude\]"` should find everything you wrote.

## Progress files

Each lesson folder may have a `progress.md`, maintained by the agent (not me). It records
what's been covered, quiz questions I got wrong or was shaky on, and what to revisit.
Read it before tutoring or quizzing in that folder. Use `/quiz` to be examined.
Its `Position:` line says how far I am (video timestamp or paper section); update it when I
mention where I am, so quizzes never run ahead of me.

Keep it current during free-form discussion too, not only in `/quiz`: when a back-and-forth
shows a misconception, or something only clicked after several rounds, add a one-line item to
"Revisit" (what I got wrong + the correct idea, dated). File it in the `progress.md` of the lesson
the concept belongs to, even if we're in a later lesson. Do it at a natural pause with a small
edit, mention it in one short line, and don't interrupt the flow.

## Git

- Work directly on `main`. No branches or PRs.
- **Commit your own bookkeeping automatically, without asking**: `progress.md` updates
  (after a quiz or a discussion) and overview READMEs. Stage only those files, then mention
  the commit in one line.
- My lesson code: only commit when I ask, or offer to at natural checkpoints (finished a
  lesson section). Never commit half-broken code without saying so.
- Don't push unless I ask (`/finish-lesson` pushes).
- One commit per meaningful step, scoped to one lesson folder where possible.
- Message format: `<lesson>: <what>`, e.g. `makemore-mlp: add embedding + hidden layer`.
  Imperative, lowercase, short.
- `progress.md` updates go in their own commit: `<lesson>: quiz progress`.
- Don't commit large datasets, model checkpoints, PDFs, or outputs — add them to `.gitignore`.
- Never rewrite history (rebase, amend, force-push) unless I ask.
