# claude-tutor

Learn from courses and papers with [Claude Code](https://claude.com/claude-code) as your
tutor. You write the code. Claude gives hints before answers, quizzes you, and records what
you got wrong, so that later quizzes ask it again.

## Setup

1. Click "Use this template" on GitHub, and clone your copy.
2. Run `uv sync` in the repo root.
3. Open Claude Code in the repo root.

## Usage

Run one Claude Code session per lesson, from the repo root. A lesson is a video or chapter
of a course, or a paper.

| Command | When |
|---------|------|
| `/start-lesson <course, lesson or paper>` | You begin something new. Claude sets up its folder and `progress.md`, and briefs you on what to watch for. |
| `/dive-into [question]` | A question or tangent comes up along the way. Claude follows it with you and brings you back to where you were. |
| `/quiz` | After a section, or at the end of the lesson. Claude quizzes you on the lesson and on earlier lessons, and records what you got wrong. |
| `/quiz review` | After a break. Claude quizzes you on the whole course, with no new material. |
| `/finish-lesson` | You are at the end of the lesson. Claude marks it done, commits, pushes, and names the next lesson. |

Between commands, ask Claude anything. It answers with hints first and writes code only
when you ask.

## Example: one lesson, from start to finish

This shows how to use claude-tutor with Andrej Karpathy's
[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html). Its roadmap is in
[`courses/zero-to-hero/`](courses/zero-to-hero/).

### Start the lesson

```
> /start-lesson zero-to-hero 01
```

Claude creates `courses/zero-to-hero/01-micrograd/` with a `progress.md` and an empty
`main.py`. It marks lesson 01 as in progress in the course roadmap and briefs you:

```
What you build: a scalar Value class that records the operations that produced it and
can backpropagate gradients through them.

Concepts to watch for
1. The derivative as sensitivity: (f(x+h) − f(x))/h.
2. The chain rule as local × upstream: ∂L/∂x = ∂L/∂out · ∂out/∂x.
3. Gradient accumulation with +=, when a value is used more than once.
...
```

### Ask for help

You follow the lesson and write the code. When you are stuck, ask:

```
> my loss doesn't go down after the first step, what's wrong?

Look at line 42. What does p.grad hold when loss.backward() runs in the second step?
```

Claude gives a hint first, then a bigger hint, then the answer.

### Dive into a tangent

A question comes up along the way. For example, a quiz question about train and test data
makes you wonder what the difference between covariate shift and label shift is. Dive into
it without losing track of where you were:

```
> /dive-into what's the difference between covariate shift and label shift?
```

Each follow-up question opens a new branch. Claude keeps track of the open ones and shows
the tree when you ask "where were we?":

```
Quiz (review 01–03): Q5 open
└─ covariate shift vs. label shift
   ├─ ✓ covariate shift: p(x) changes, p(y|x) stays the same
   └─ ▸ label shift: p(y) changes, p(x|y) stays the same (check question open)
```

When every branch is settled, Claude quizzes you on the tangent and brings you back up to
where you were, here quiz question 5.

### Get quizzed

```
> /quiz
```

Claude shows where you stand, then asks about six questions, one at a time:

```
01 — micrograd
  ████████████░░░░░░░░  60%   ~87 / 145 min
  ✓ Value · chain rule · backward ▸ neuron · MLP · training loop

Course  ◐ 01  ○ 02  ○ 03  ○ 04  ○ 05  ○ 06  ○ 07  ○ 08  ○ 09
Revisit  01: 2 open   last quiz: 10-14
```

Most questions are about the current lesson and your code. The rest review earlier lessons.
Claude writes what you got wrong to "Revisit" in `progress.md`:

```markdown
## Revisit
- Chain rule for a new op: wrote `1 * self.data` instead of `out.grad * local` (2026-10-14) (asked 10-16 ✓)
```

Later quizzes ask the "Revisit" items again. An item leaves "Revisit" after you answer it
right on two different days.

### Finish the lesson

```
> /finish-lesson
```

Claude checks that your last quiz was at the end of the lesson, marks the lesson done in the
roadmap, commits, pushes, and names the next lesson.

## Reading a paper

A paper is a lesson too:

```
> /start-lesson https://arxiv.org/abs/1706.03762
```

Claude adds the paper to a reading list in `papers/<topic>/README.md` and creates
`papers/<topic>/<year>-<short-name>/` for your notes and code. `uv run papers/fetch.py`
downloads the PDF of every paper on the reading lists into `papers/<topic>/pdfs/`, which git
ignores.

## Layout

```
courses/<course>/README.md               roadmap of the course
courses/<course>/<NN-topic>/             your code and progress.md for one lesson
papers/<topic>/README.md                 reading list
papers/<topic>/<year>-<short-name>/      your notes and code for one paper
.claude/skills/                          the commands above
CLAUDE.md                                the rules Claude follows in this repo
```

`CLAUDE.md` holds rules such as "Don't write my implementation for me unless I explicitly
ask". Edit them to change how Claude tutors you.

## Courses

- [Neural Networks: Zero to Hero](courses/zero-to-hero/) (Karpathy). Currently on: not started.

## Papers

Reading lists by topic, in `papers/<topic>/README.md`.
