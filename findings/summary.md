# 📊 Benchmarking Summary: Local LLM with GuideLLM

This document summarizes the benchmarking experiments conducted on a locally hosted LLM (`liquid/lfm2-1.2b Q8_0` via LM Studio) using [GuideLLM](https://github.com/chaoyi-wu/GuideLlm).  
The goal was to evaluate performance under different benchmark strategies: **synchronous**, **throughput**, and **constant**.

---

## 🧪 Setup
- **Model:** `liquid/lfm2-1.2b Q8_0` (quantized, hosted via LM Studio)
- **Benchmark tool:** GuideLLM
- **Environment:** WSL Ubuntu, local HTTP endpoint (`http://localhost:1234/v1`)
- **Dataset:** `embedding.txt` (5–10 prompts, one per line)
- **Profiles tested:** `--synchronous`, `--throughput`, `--profile sweep constant`

---

## 📈 Results Overview

### ✅ Synchronous Mode
- **Completions:** 6/6 successful
- **Latency:** Median ~22.8s
- **TTFT (Time to First Token):** ~884ms
- **ITL (Inter-Token Latency):** ~85ms
- **Tokens/sec:** ~11.2 generated
- **Errors:** 0
- **Interpretation:** Most stable mode, consistent throughput, reliable for sequential testing.

---

### ⚡ Throughput Mode
- **Completions:** 4 successful, 2 errors
- **Latency:** ~12s median (but variable)
- **TTFT:** ~1008ms
- **Concurrency:** ~2.2
- **Tokens/sec:** ~11.2 generated, ~12.5 total
- **Interpretation:** Faster than synchronous, but prone to errors under load.

---

### 🔄 Constant Mode (Sweep)
- **Completions:** 5–6 per run
- **Errors:** Up to 229 in some runs
- **Latency:** Highly variable (1.5s – 25s+)
- **TTFT:** Spikes up to 9.7s
- **Tokens/sec:** 5.7 – 11.4 depending on run
- **Interpretation:** Unstable with current backend; concurrency overload and client disconnects observed.

---

## 📊 Key Metrics

| Strategy     | Latency (Mdn) | TTFT (Mdn) | Gen Speed (tok/s) | Errors |
|--------------|---------------|------------|--------------------|--------|
| Synchronous  | 22.8s         | 884ms      | 11.2               | 0      |
| Throughput   | 12s           | 1008ms     | 11.2               | 2      |
| Constant@0   | 1.5–25s       | 995–9743ms | 5.7–11.4           | 200+   |

---

## 🧠 Learnings
- **Synchronous mode** is the most reliable for local LM Studio runs.
- **Throughput mode** offers better speed but introduces instability.
- **Constant mode** is unsuitable without tuning; LM Studio struggles with concurrency and long TTFT.
- **File formatting matters:** `.txt` must be clean (UTF‑8, no blank lines).
- **JSONL datasets** must follow strict schema (`{"prompt": "...", "expected": "..."}` per line).

---

## 🚀 Next Steps
- Tune `max_tokens` in LM Studio to reduce latency and prevent disconnects.
- Experiment with smaller models for faster synchronous runs.
- Explore batching or async profiles once backend stability improves.
- Automate Hugging Face dataset conversion (`hf_to_txt.py`) for reproducible benchmarks.

---