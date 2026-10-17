---
name: finish-lesson
description: Finish the current lesson or paper — make sure it's been quizzed, mark it done in the overviews, commit and push, and say what's next. Use when I say /finish-lesson, "wrap up", "I'm done with this lesson", or "finish this part".
---

# Finish lesson

Close out the current lesson or paper. Argument: the folder; otherwise use the one we've
been working in, and confirm if unclear.

## 1. Check understanding

Read the folder's `progress.md`. Confirm `Position:` is at the end of the lesson/paper (ask me
if unsure) — otherwise it isn't done. If no quiz log entry was taken at the end position, run
the `quiz` skill first; a mid-lesson quiz doesn't count. If "Revisit" still has important items, tell me and ask whether to wrap
anyway or keep working.

## 2. Check the code

Run it (`uv run <file>`) if it's quick. If it's broken or unfinished, tell me and ask
whether to wrap anyway; if yes, the commit message must say so (e.g. "(wip)").

## 3. Update overviews

- Mark the lesson `[x]` in the course `README.md` roadmap (for a paper: set its row in
  `papers/<topic>/README.md` to `read` or `reimplemented`).
- Update "Currently on" in the root `README.md` to the next lesson.

## 4. Commit and push

Follow the Git rules in `CLAUDE.md`:
1. Code commit: `<lesson>: <what was built>`
2. Progress commit: `<lesson>: quiz progress` (`progress.md` + README updates)

Then `git push`. If the push is rejected, stop and tell me — never force-push.

## 5. What's next

One or two lines: the next lesson according to the roadmap, and anything from "Revisit" to keep in mind.
Suggest starting it in a fresh session with `/start-lesson`.
