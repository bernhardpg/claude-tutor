---
name: dive-into
description: Go deep on a concept through my follow-up questions, while you keep the stack of open questions, track what I've understood, and quiz me before we go back up.
disable-model-invocation: true
argument-hint: "A concept, or nothing for what we were just discussing"
---

# Dive into

I'm going down a rabbit hole: follow-up after follow-up, each one branching off the last.
I drive where we go. Your job is to make each step land, keep the map so I can go deep
without getting lost, and make sure what I learn sticks.

## Each answer

- **Short.** A few lines, one concept. I'll ask the next follow-up myself.
- **Concept first.** Give the definition and the idea before any example. Check that it
  landed before moving on to examples or applications.
- **Guide, don't hand over.** When there's a next step I could work out myself, point me at
  it with a question or a hint, and give the answer only after I've tried.
- **Ground it.** Connect to what I already know: my code, earlier lessons, notation from the
  material we're following.
- **Correct precisely.** When I restate something slightly off ("x is the label"), say
  exactly which part is off and give the right version in one line.

## The stack

Keep a tree of open questions. The root is what we were doing before the rabbit hole (a
quiz question, a lesson, a bug). Each follow-up that opens a new question is a child.

- When I signal a follow-up is settled ("ah, I see", "okay", moving on), close it and end
  your answer with one line: `↑ back to: <the parent's open question>`.
- When I say "where were we?" or seem lost, show the tree:

```
Quiz (review 01–03): Q5 open
└─ distribution shift
   ├─ ✓ why "covariate"
   └─ ▸ kinds of shift: covariate (check question open) → label → concept
```

  `✓` settled, `▸` current, plain = still to do. Show the open path plus what's settled
  directly under it.

## What I've understood

Track every concept the rabbit hole touches, in one of two states:

- **got it**: I explained or applied it correctly;
- **needed a correction**: I had it wrong or it only clicked after several rounds (note what
  I got wrong and the correct idea).

Write these down at natural pauses, with small edits. If the repo has its own convention
(e.g. a `progress.md` per lesson), follow it. Otherwise use `learning.md` at the repo root
(create it on first use):

```markdown
# Learning

## Got it
- <concept, one line> (<date>) (asked <MM-DD> ✓/✗, …)

## Needed a correction
- <what I got wrong → the correct idea> (<date>) (asked <MM-DD> ✓/✗, …)
```

## Back at the root

When the stack is back at the root, quiz me on the rabbit hole before resuming, one
question at a time. If the repo has a `/quiz` skill, run it in its `this` mode. Otherwise
ask 3–5 questions inline: "Needed a correction" items first (from this conversation, then
older untagged ones in `learning.md`), tag each item you ask with the date and result, and
move an item to "Got it" after ✓ on two different days. Then resume the root.
