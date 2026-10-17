---
name: quiz
description: Quiz me on the lesson or paper I'm currently working on, mixed with spaced review of earlier lessons in the same course, then record weak spots in progress.md. Use when I say /quiz, "quiz me", "test me", or "check my understanding". `/quiz review` quizzes the whole course with no new material.
---

# Quiz

Examine my understanding of the current lesson, mixed with spaced review of earlier lessons
in the same course, then update the `progress.md` files.

## 1. Find the target

- If an argument is given (a folder path or topic), use it.
- `/quiz review [course]`: whole-course review, no current lesson. All questions come from
  the review pool (step 2).
- `/quiz this`: only what came up in this conversation: the items it added or changed in any
  `progress.md`, Revisit items first. Skip the review pool; ask as many questions as there
  are items worth checking (up to ~6).
- Otherwise use the lesson folder I've most recently been working in (the file open in my
  IDE, or the files discussed in this conversation). If unclear, ask which one.

## 2. Gather context

- Read my code in that folder.
- Read `progress.md` if it exists — **start with the items under "Revisit"**.
- **Scope to where I am.** Current-lesson questions cover only material up to the
  `Position:` line, plus "Covered" and what we've discussed this session — never ahead of
  it. If Position is missing, or my code/our discussion suggests I've moved past it, ask
  where I am first (video timestamp or paper section) and update it. Mid-lesson quizzes are
  normal.
- Identify the source (e.g. which Karpathy video, which paper) and what it covers.
  Use your own knowledge of the material; I don't keep notes.
- **Review pool:** read `progress.md` of every earlier lesson in the same course (never other
  courses or papers). Pick review items in this order:
  1. open "Revisit" items, least recently asked first (untagged = never asked);
  2. "Covered" items never quizzed (no `asked` tag).

## 3. Show where I stand

Before the first question, show a short status block (from the `progress.md` files):

```
03 — makemore 2: MLP
  ███░░░░░░░░░░░░░░░░░  15%   ~12 / 75 min
  ✓ dataset  ▸ embedding · hidden layer · cross-entropy · minibatch · lr search · splits

Course  ● 01  ● 02  ◐ 03  ○ 04  ○ 05  ○ 06  ○ 07  ○ 08  ○ 09
Revisit  01: 5 open   02: 5 open   03: 0     last quiz: —
```

- **Bar:** 20 cells of `█`/`░`, filled by position ÷ video length (or sections read ÷ total
  for a paper), with the percentage and the raw numbers.
- **Milestones:** the lesson's main topics in order (from the course README's key concepts),
  `✓` done, `▸` next, `·` still ahead.
- **Course:** `●` done, `◐` current, `○` not started (from the course roadmap).
- **Revisit:** number of open items per lesson.

Then start.

## 4. Ask questions — one at a time

Ask ~6 questions (fewer if I ask for a quick one), **one per message**, and wait for my answer
before continuing. Never reveal the answer before I've tried.

- **Mix:** ~4 on the current lesson, ~2 from the review pool, interleaved (not all review at
  the end). Don't say which is which — picking the right idea is part of the test.
- **Linking questions:** now and then, ask one that connects lessons, e.g. "how does your
  hand-written NLL in 02 relate to `F.cross_entropy` in 03?"

Mix of question types:
- **About my code**: "What's the shape of X on line N?", "Why this and not that?",
  "What breaks if you change Y?", "Predict the output / initial loss".
- **Concepts**: the ideas the lesson teaches, the math behind them, why they work.
- **Transfer**: apply the idea to a slightly new situation, or connect it to modern practice.

Tune difficulty: if I answer easily, go deeper; if I struggle, give a hint and break the
question into smaller steps. After each answer: say whether it was right, fill in anything
missing or imprecise in 1–3 sentences, then ask the next question.

## 5. Wrap up

Give a short summary: what I clearly understand, what's shaky, and 1–2 concrete things to try
in code to solidify the shaky parts.

## 6. Update `progress.md`

Update the current lesson's `progress.md` and, for review questions, the `progress.md` of the
lesson each item came from. Keep it short — it's for you, the agent, next time.

- **Tag every item you asked about** with the date and result, appending to any existing tag:
  `(asked 10-01 ✗, 10-04 ✓)`. The tags drive the spacing in step 2.
- **Graduate** a Revisit item to Covered after ✓ on two different days (keep its tag).
- A ✗ on a Covered item moves it back to Revisit.

Format:

```markdown
# Progress: <lesson name>

Source: <link or name>
Position: <video timestamp / paper section + what's there>, <date>

## Covered
- <topics implemented / understood>

## Revisit
- <concept or question I got wrong or was shaky on> (<date>) (asked <MM-DD> ✓/✗, …)

## Quiz log
- <date> (at <position>): <n> questions (<k> review), <one-line summary>
```
