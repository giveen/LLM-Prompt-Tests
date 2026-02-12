# Security Benchmark Tool - Setup Guide

This guide will help you set up and run the Security Benchmark Tool for evaluating LLMs on cybersecurity tasks.

## Quick Start

### 1. Automated Setup (Recommended)

Run the setup script to automatically install all dependencies:

```bash
./setup.sh
```

This script will:
- Check Python version
- Create a virtual environment
- Install all required packages
- Create a `.env` file from template

### 2. Manual Setup

If you prefer to set up manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

## Configuration

### Environment Variables

Edit the `.env` file and add your API keys for the LLM providers you want to use:

```bash
# For OpenAI models
OPENAI_API_KEY=sk-...
OPENAI_API_BASE=https://api.openai.com/v1

# For Anthropic models
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_API_BASE=https://api.anthropic.com

# For Azure OpenAI
AZURE_API_KEY=...
AZURE_API_BASE=https://your-resource.openai.azure.com

# For local Ollama models
OLLAMA_API_BASE=http://localhost:11434
```

## Usage

The main evaluation script is `eval2.py`. Here's how to use it:

### Basic Syntax

```bash
python eval2.py -d DATASET_FILE -e EVAL_TYPE -B BACKEND -m MODEL [-s SAVE_INTERVAL]
```

### Parameters

- `-d, --dataset_file`: Path to the dataset file
- `-e, --eval`: Evaluation type (`seceval`, `cybermetric`, or `cti_bench`)
- `-B, --backend`: LLM backend (`openai`, `anthropic`, `azure`, `ollama`)
- `-m, --model`: Model name (e.g., `gpt-4`, `claude-3-opus-20240229`)
- `-s, --save_interval`: (Optional) Save intermediate results every N questions

### Available Datasets

#### SecEval
```bash
# Dataset 1
python eval2.py -d utils/seceval_dataset/questions.json -e seceval -B openai -m gpt-4

# Dataset 2
python eval2.py -d utils/seceval_dataset/questions-2.json -e seceval -B openai -m gpt-4
```

#### CyberMetric
```bash
python eval2.py -d utils/cybermetric_dataset/CyberMetric-2-v1.json -e cybermetric -B openai -m gpt-4
```

#### CTI Bench
```bash
# Multiple CTI benchmark datasets available
python eval2.py -d utils/cti_bench_dataset/cti-mcq1.tsv -e cti_bench -B openai -m gpt-4
python eval2.py -d utils/cti_bench_dataset/cti-ate2.tsv -e cti_bench -B openai -m gpt-4
python eval2.py -d utils/cti_bench_dataset/cti-rcm2.tsv -e cti_bench -B openai -m gpt-4
python eval2.py -d utils/cti_bench_dataset/cti-vsp2.tsv -e cti_bench -B openai -m gpt-4
```

### Example Commands

#### Using OpenAI GPT-4
```bash
python eval2.py \
  -d utils/seceval_dataset/questions.json \
  -e seceval \
  -B openai \
  -m gpt-4 \
  -s 10
```

#### Using Anthropic Claude
```bash
python eval2.py \
  -d utils/cybermetric_dataset/CyberMetric-2-v1.json \
  -e cybermetric \
  -B anthropic \
  -m claude-3-opus-20240229 \
  -s 10
```

#### Using Local Ollama Model
```bash
python eval2.py \
  -d utils/seceval_dataset/questions.json \
  -e seceval \
  -B ollama \
  -m llama2 \
  -s 5
```

## Output

### Results
- Results are saved to JSON files in the current directory
- Filename format: `benchmark_results_{eval_type}_{model_name}.json`
- Contains all questions, model answers, and correct solutions

### Checkpoints
- Intermediate results are saved in the `checkpoints/` directory
- Saved every N questions (if `-s` flag is used)
- Useful for resuming long evaluations

### Cost Tracking
- The script tracks token usage and estimates costs
- Automatic cost cap of $20 to prevent accidental overspending
- Fetches current pricing from LiteLLM pricing database

## Troubleshooting

### Python Version
Ensure you have Python 3.8 or higher:
```bash
python3 --version
```

### Missing Dependencies
If you encounter import errors:
```bash
pip install --upgrade -r requirements.txt
```

### API Key Issues
Check that your `.env` file has the correct API keys and they're loaded:
```bash
# Test if environment variables are set
source venv/bin/activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"
```

### Model Not Found
Ensure you're using the correct model name for your provider:
- OpenAI: `gpt-4`, `gpt-3.5-turbo`, etc.
- Anthropic: `claude-3-opus-20240229`, `claude-3-sonnet-20240229`, etc.
- Ollama: Check available models with `ollama list`

## Advanced Features

### Custom Checkpointing
Save intermediate results every 5 questions:
```bash
python eval2.py -d dataset.json -e seceval -B openai -m gpt-4 -s 5
```

### Using Different Backends
The tool supports multiple LLM backends through LiteLLM:
- OpenAI
- Anthropic
- Azure OpenAI
- Ollama (local models)
- And many more (see [LiteLLM docs](https://docs.litellm.ai/docs/))

## Project Structure

```
security-benchmarks/
├── eval2.py                 # Main evaluation script ⭐
├── eval_original.py         # Original eval.py (reference)
├── requirements.txt         # Python dependencies
├── setup.sh                # Automated setup script
├── .env.example            # Environment variable template
├── .env                    # Your API keys (create this)
├── README.md               # Project documentation
├── SETUP.md                # This file
├── checkpoints/            # Intermediate results
└── utils/                  # Datasets and resources
    ├── seceval_dataset/
    ├── cybermetric_dataset/
    └── cti_bench_dataset/
```

## Need Help?

- Check the main [README.md](README.md) for more information about the benchmarks
- Review the original CAIBench documentation
- Open an issue if you encounter problems

## License

See the main project README for license information.
