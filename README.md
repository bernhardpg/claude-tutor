# claude-tutor

A repo for learning ML (or anything with code) by following courses and reading papers, with
[Claude Code](https://claude.com/claude-code) as tutor and examiner. You write the code;
Claude gives hints instead of answers, quizzes you with spaced review, and keeps track of
what you got wrong in a `progress.md` per lesson.

## Setup

1. Click "Use this template" on GitHub (or clone), then:
   ```sh
   uv sync
   ```
2. Open Claude Code at the repo root and run `/start-lesson zero-to-hero 01`, or
   `/start-lesson <link to a course or paper>`.

`CLAUDE.md` holds the rules Claude follows here (tutor mode, how progress is tracked, git
conventions). Edit it to taste.

## Workflow

One Claude Code session per lesson, started from the repo root:

| Skill | When |
|-------|------|
| `/start-lesson <lesson/course/paper>` | Begin something new: sets up the folder and `progress.md`, briefs you on what to watch for |
| `/quiz` | After a section, or at the end: tests the lesson plus spaced review of earlier lessons, saves weak spots |
| `/quiz review` | After a break: whole-course review, no new material |
| `/dive-into [concept]` | When follow-up questions pile up: keeps the stack of open questions, quizzes you before going back |
| `/finish-lesson` | Lesson done: checks it was quizzed, marks it done, commits and pushes, suggests what's next |

The skills live in `.claude/skills/`.

## Layout

- `courses/<course>/` — a `README.md` roadmap plus one folder per lesson, each with your
  code and a `progress.md`. [`courses/zero-to-hero/`](courses/zero-to-hero/) is an example.
- `papers/<topic>/` — a `README.md` reading list; papers you dig into get their own folder.
  `uv run papers/fetch.py` downloads the PDFs from the reading lists (gitignored).

## Courses

- [Neural Networks: Zero to Hero](courses/zero-to-hero/) (Karpathy). Currently on: not started.

## Papers

Reading lists by topic, in `papers/<topic>/README.md`.
