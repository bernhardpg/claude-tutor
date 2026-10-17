# Neural Networks: Zero to Hero (Karpathy)

**Goal:** reproduce GPT-2 (124M) from scratch (lesson 09).
Course page with all videos: https://karpathy.ai/zero-to-hero.html · Code: https://github.com/karpathy/nn-zero-to-hero

## Roadmap

Status: `[ ]` not started · `[~]` in progress · `[x]` done (quizzed with `/quiz`, closed with `/finish-lesson`)

| # | Lesson | Length | Folder | Status | Needed for GPT-2? |
|---|--------|--------|--------|--------|-------------------|
| 01 | micrograd: backprop from scratch | 2h25 | `01-micrograd/` | [ ] | **Core** |
| 02 | makemore 1: bigram language model | 1h57 | `02-makemore-bigram/` | [ ] | **Core** |
| 03 | makemore 2: MLP | 1h15 | `03-makemore-mlp/` | [ ] | **Core** |
| 04 | makemore 3: activations, gradients, BatchNorm | 1h55 | `04-makemore-batchnorm/` | [ ] | **Core** |
| 05 | makemore 4: backprop ninja | 1h55 | `05-makemore-backprop-ninja/` | [ ] | Recommended |
| 06 | makemore 5: WaveNet | 0h56 | `06-makemore-wavenet/` | [ ] | Optional |
| 07 | Let's build GPT from scratch | 1h56 | `07-gpt-from-scratch/` | [ ] | **Core** |
| 08 | Let's build the GPT tokenizer | 2h13 | `08-gpt-tokenizer/` | [ ] | Recommended |
| 09 | Let's reproduce GPT-2 (124M) | 4h01 | `09-reproduce-gpt2/` | [ ] | 🎯 Goal |

The core lessons alone are about 14h of video. Expect 2–3× that with implementation.

## Where to start

**Start at 01 (micrograd), then do 02 before continuing 03.** The MLP lesson assumes the
bigram lesson: character encoding, `names.txt`, turning counts into probabilities, NLL loss and the
training loop all come from it, and the MLP lesson moves fast through them.
micrograd is what makes `loss.backward()` stop being magic. Everything after it builds on it.

If you already know backprop and computational graphs well, you can go quickly through 01:
watch it at 1.5×, write the `Value` class, and move on. Don't skip it entirely.

**Minimum path to GPT-2:** 01 → 02 → 03 → 04 → 07 → 09. Do 08 before 09 if you want to
understand tokenization rather than treat `tiktoken` as a black box.

## Lessons

### 01 — micrograd
Build a tiny autograd engine (a `Value` scalar class) and a small neural net library on top of it.
- **Key concepts:** derivatives as sensitivity, computational graph, chain rule, backprop via topological
  sort, gradient accumulation (`+=`), zeroing grads, a neuron/layer/MLP, gradient descent.
- **Done when:** your MLP trains on a toy dataset with *your* `Value.backward()`, and you can
  verify gradients against PyTorch.
- Repo: https://github.com/karpathy/micrograd

### 02 — makemore 1: bigram
Character-level model of names: first by counting, then as a one-layer neural net.
- **Key concepts:** tokenization at the character level, bigram counts → probabilities,
  sampling with `torch.multinomial`, likelihood / negative log-likelihood, smoothing,
  one-hot encoding, softmax, broadcasting rules (a classic bug is shown in the video), regularization.
- **Done when:** the counting model and the neural-net model reach the same loss (~2.45).
- Repo: https://github.com/karpathy/makemore

### 03 — makemore 2: MLP
Bengio et al. 2003: embed the previous 3 characters, hidden tanh layer, predict the next.
- **Key concepts:** embedding table, context window, `view` / tensor internals,
  `F.cross_entropy`, minibatching, learning-rate search, train/dev/test split,
  underfitting vs. overfitting, scaling up embedding and hidden sizes.
- **Done when:** dev loss is about 2.2 or lower, and the samples look name-like.

### 04 — makemore 3: activations, gradients, BatchNorm
Why deep nets are hard to train and how to diagnose them.
- **Key concepts:** loss at initialization (should be about −log(1/27)), saturated tanh, dead neurons,
  Kaiming initialization, BatchNorm (train vs. eval, running stats), activation/gradient
  histograms, update-to-data ratio, rewriting the code as `nn.Module`-style layers.
- **Done when:** you can read the diagnostic plots and explain what a bad one means.

### 05 — makemore 4: backprop ninja
Backprop through the whole MLP + BatchNorm by hand, at the tensor level.
- **Key concepts:** manual gradients for matmul, broadcasting, sums, cross-entropy
  (the simplified formula), BatchNorm backward; checking against autograd.
- **Why recommended:** it's hard, but it builds the tensor-shape intuition you'll need for 07 and 09.

### 06 — makemore 5: WaveNet
Deeper, hierarchical model that combines context progressively. More `nn.Module`-style code.
- **Key concepts:** hierarchical/dilated structure, `Sequential`, `FlattenConsecutive`,
  BatchNorm with 3D inputs, a typical deep-learning development workflow.
- **Optional:** useful practice, but 07 doesn't depend on it.

### 07 — Let's build GPT
A decoder-only Transformer trained on Tiny Shakespeare (becomes nanoGPT).
- **Key concepts:** self-attention (Q, K, V), causal masking, the averaging-with-matmul trick, scaled attention,
  multi-head attention, feed-forward, residual connections, LayerNorm (pre-norm), dropout,
  positional embeddings.
- **Done when:** your model generates Shakespeare-ish text and you can write attention
  from memory.
- Repo: https://github.com/karpathy/nanoGPT

### 08 — GPT tokenizer
Byte Pair Encoding from scratch; why tokenization causes many LLM quirks.
- **Key concepts:** Unicode/UTF-8, BPE training (merges), encode/decode, the regex
  pre-tokenizer used in GPT-2/4, special tokens, `tiktoken` and `sentencepiece`.
- **Done when:** your BPE tokenizer matches `tiktoken`'s GPT-2 encoding on test strings.
- Repo: https://github.com/karpathy/minbpe

### 09 — Reproduce GPT-2 (124M) 🎯
Build GPT-2 to match HuggingFace weights, then train it from scratch on FineWeb-Edu.
- **Key concepts:** loading pretrained weights, weight tying, initialization,
  mixed precision (TF32/bf16), `torch.compile`, flash attention, "nice numbers" for tensor sizes,
  AdamW + gradient clipping, cosine LR schedule, gradient accumulation, DDP (multi-GPU),
  HellaSwag evaluation.
- **Compute:** you can do the first half (architecture, loading weights, small overfitting runs)
  on your Mac using `mps`. The full training run needs a cloud GPU: he uses 8×A100 for about 1h;
  a single rented GPU works if you train longer or on less data.
- Repo: https://github.com/karpathy/build-nanogpt

## Workflow per lesson

1. `/start-lesson zero-to-hero NN`, then watch and implement along with the video. Pause often
   and try the next step yourself before he shows it.
2. Do the exercises in the video description, if there are any.
3. `/quiz` along the way, then `/finish-lesson` once you're at the end.
