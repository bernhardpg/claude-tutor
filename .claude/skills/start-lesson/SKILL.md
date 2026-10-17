---
name: start-lesson
description: Start a new lesson, course, or paper — set up the folder, progress.md, and overviews, then brief me on what to watch for. Use when I say /start-lesson, "start lesson X", "let's begin <course>", or share a new course/paper link to work through.
---

# Start lesson

Set up something new to learn, then brief me. Argument: a lesson ("zero-to-hero 01"),
a new course (name or URL), or a paper (arXiv link or title). If missing, suggest the next
lesson from the current course overview and confirm.

Lesson numbers are **absolute roadmap numbers** (the `#` column), not the video's own
title: "makemore part 3" means roadmap 03, not the video titled "makemore Part 3" (04).
If it's still ambiguous, check which lesson is `[~]` and confirm.

## 1. Identify what it is

- **Lesson in an existing course** → `courses/<course>/NN-<topic>/`, numbered as in that
  course's `README.md` roadmap.
- **New course** → `courses/<course-slug>/` plus a course `README.md` overview
  (see step 3), then set up its first lesson.
- **Paper** → `papers/<topic>/<year>-<short-name>/`. Pick the topic with me; if it's new,
  create `papers/<topic>/README.md` (reading list, see `CLAUDE.md`).

If a folder already exists, don't recreate it — say so and just brief me.

## 2. Create the folder

- `progress.md` using the format in the `quiz` skill (Source line with link, empty sections).
- A minimal `main.py` stub only if the lesson involves code — just imports and an empty
  `main()`, no implementation (I write the code).
- Data the lesson needs (e.g. `names.txt`): download it if it's small and public; if over a few
  MB, add it to `.gitignore`. If unsure where it comes from, tell me instead of guessing.
- New dependencies: `uv add <pkg>`.

## 3. Update overviews

- **New course**: write `courses/<course>/README.md` modeled on
  `courses/zero-to-hero/README.md` — goal, roadmap table (status, folder, core/optional),
  where to start, per-lesson key concepts + "done when". Verify the lesson list against the
  actual course page rather than memory when possible. Add the course to the root `README.md`.
- **Lesson**: mark it `[~]` in the course roadmap and update "Currently on" in the root README.
- **Paper**: set its row in `papers/<topic>/README.md` to `reading` and link the folder;
  add the topic under "Papers" in the root README if it's new.

## 4. Brief me (short)

- What this lesson/paper builds, in 1–2 sentences.
- 3–5 concepts to watch for.
- Prerequisites worth refreshing — check earlier lessons' `progress.md` "Revisit" items and
  mention any that matter here.
- Practical notes (compute, data, gotchas).

Don't commit — `/finish-lesson` handles that, or I'll ask.

