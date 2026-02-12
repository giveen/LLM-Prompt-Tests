# Quick Reference Guide

## 🚀 Quick Start

```bash
# 1. Run setup (installs everything)
./setup.sh

# 2. Add your API keys to .env
nano .env

# 3. Activate virtual environment
source venv/bin/activate

# 4. Run evaluation
python eval2.py -d utils/seceval_dataset/questions.json -e seceval -B openai -m gpt-4
```

## 📋 Common Commands

### SecEval Benchmark
```bash
python eval2.py -d utils/seceval_dataset/questions.json -e seceval -B openai -m gpt-4 -s 10 --status-interval 10
python eval2.py -d utils/seceval_dataset/questions-2.json -e seceval -B openai -m gpt-4 -s 10 --status-interval 10
```

### CyberMetric Benchmark
```bash
python eval2.py -d utils/cybermetric_dataset/CyberMetric-2-v1.json -e cybermetric -B openai -m gpt-4 -s 10 --status-interval 10
```

### CTI Bench
```bash
python eval2.py -d utils/cti_bench_dataset/cti-mcq1.tsv -e cti_bench -B openai -m gpt-4 -s 10 --status-interval 10
python eval2.py -d utils/cti_bench_dataset/cti-ate2.tsv -e cti_bench -B openai -m gpt-4 -s 10 --status-interval 10
```

## 🎯 Using Different Models

### OpenAI
```bash
# GPT-4
python eval2.py -d DATASET -e TYPE -B openai -m gpt-4 --status-interval 10

# GPT-3.5 Turbo
python eval2.py -d DATASET -e TYPE -B openai -m gpt-3.5-turbo --status-interval 10
```

### Anthropic
```bash
# Claude Opus
python eval2.py -d DATASET -e TYPE -B anthropic -m claude-3-opus-20240229 --status-interval 10

# Claude Sonnet
python eval2.py -d DATASET -e TYPE -B anthropic -m claude-3-sonnet-20240229 --status-interval 10
```

### Ollama (Local)
```bash
# Llama 2
python eval2.py -d DATASET -e TYPE -B ollama -m llama2 --status-interval 10

# Mistral
python eval2.py -d DATASET -e TYPE -B ollama -m mistral --status-interval 10

# Qwen3 8B Heretic
python eval2.py -d DATASET -e TYPE -B ollama -m svjack/Qwen3-8B-heretic:latest --status-interval 10
```

## 📊 Available Datasets

| Benchmark | Dataset File | Type |
|-----------|--------------|------|
| SecEval | `utils/seceval_dataset/questions.json` | `seceval` |
| SecEval 2 | `utils/seceval_dataset/questions-2.json` | `seceval` |
| CyberMetric | `utils/cybermetric_dataset/CyberMetric-2-v1.json` | `cybermetric` |
| CTI MCQ | `utils/cti_bench_dataset/cti-mcq1.tsv` | `cti_bench` |
| CTI ATE | `utils/cti_bench_dataset/cti-ate2.tsv` | `cti_bench` |
| CTI RCM | `utils/cti_bench_dataset/cti-rcm2.tsv` | `cti_bench` |
| CTI VSP | `utils/cti_bench_dataset/cti-vsp2.tsv` | `cti_bench` |

## 🔧 Parameters

### Required Parameters
- `-d` : Dataset file path
- `-e` : Evaluation type: `seceval`, `cybermetric`, or `cti_bench`
- `-B` : Backend/provider: `openai`, `anthropic`, `azure`, `ollama`
- `-m` : Model name

### Optional Parameters
- `-s` : Save checkpoint every N questions
- `--status-interval` : Print status update every N seconds

### Model Parameters
Use these to control model behavior:
- `--temperature FLOAT` : Temperature (0.0-2.0, controls randomness)
- `--max-tokens INT` : Maximum tokens in response
- `--top-p FLOAT` : Nucleus sampling (top-p)
- `--top-k INT` : Top-k sampling
- `--frequency-penalty FLOAT` : Frequency penalty (-2.0 to 2.0)
- `--presence-penalty FLOAT` : Presence penalty (-2.0 to 2.0)

## 📈 With Progress Tracking

```bash
# Print status every 10 seconds
python eval2.py -d utils/seceval_dataset/questions.json \
  -e seceval -B ollama -m "svjack/Qwen3-8B-heretic:latest" \
  --status-interval 10 -s 50
```

Example output:
```
======================================================================
Starting Evaluation
Model: svjack/Qwen3-8B-heretic:latest
Total questions: 2000
======================================================================

[  50]  2.5% | Correct:   32 | Wrong:   18 | Accuracy:  64.00% | Time: 1m 23s | Est. remaining: 54m 12s | Cost: $0.0000
[ 100]  5.0% | Correct:   67 | Wrong:   33 | Accuracy:  67.00% | Time: 2m 45s | Est. remaining: 51m 32s | Cost: $0.0000
[ 150]  7.5% | Correct:   99 | Wrong:   51 | Accuracy:  66.00% | Time: 4m 10s | Est. remaining: 50m 18s | Cost: $0.0000
```

## 🧪 Model Parameter Examples

### Conservative/Deterministic (for consistent answers)
```bash
python eval2.py -d DATASET -e TYPE -B ollama -m llama2 \
  --temperature 0.1 --top-p 0.9 --status-interval 10
```

### Creative/Diverse (for exploration)
```bash
python eval2.py -d DATASET -e TYPE -B openai -m gpt-4 \
  --temperature 0.8 --top-p 0.95 --status-interval 10
```

### Limited Output (for faster responses)
```bash
python eval2.py -d DATASET -e TYPE -B ollama -m mistral \
  --max-tokens 100 --status-interval 10
```

## 📁 Output Files

- Results: `benchmark_results_{eval_type}_{model_name}.json`
- Checkpoints: `checkpoints/{model_name}/checkpoint_{N}.json`

## 💰 Cost Management

- Automatic $20 cost cap
- Token usage tracking
- Pricing fetched from LiteLLM database

## 🆘 Need Help?

- Full documentation: [SETUP.md](SETUP.md)
- Project info: [README.md](README.md)
- Show help: `python eval2.py -h`

## 🔑 Environment Variables

Required in `.env` file:
```bash
OPENAI_API_KEY=your_key_here
OPENAI_API_BASE=https://api.openai.com/v1

ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_API_BASE=https://api.anthropic.com

OLLAMA_API_BASE=http://localhost:11434
```
