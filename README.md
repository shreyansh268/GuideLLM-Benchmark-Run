# GuideLLM-Benchmark-Run
Project to demonstrate usage of GuideLLM open source LLM benchmarking library to run benchmark tests for a locally hosted LLM

# 🔍 Benchmarking Local LLMs with GuideLLM

This repo documents the process and findings from benchmarking a locally hosted LLM (`liquid/lfm2-1.2b` via LM Studio) using [GuideLLM](https://github.com/chaoyi-wu/GuideLlm).

## 🧪 Setup
- Model: `lfm2-1.2b Q8_0` via LM Studio
- Benchmark tool: GuideLLM
- Dataset: Custom prompts + Hugging Face conversions

## 🚀 Benchmarking Commands
```bash
guidellm benchmark --target "http://localhost:1234/v1" --profile synchronous --data benchmark/embedding.txt --max-seconds 90
guidellm benchmark --target "http://localhost:1234/v1" --profile sweep --max-seconds 300 --data benchmark/embedding.txt
```

