"""
Benchmark Evaluation Script

Evaluates language models on cybersecurity-related benchmarks:
- SecEval
- CyberMetric
- CTI Bench (MCQ)

Usage:
  python eval2.py -d DATASET -e seceval -B openai -m MODEL [-s N]
"""

import json
import re
import os
import sys
import csv
import argparse
import datetime
import time
import dotenv
import requests
import litellm

dotenv.load_dotenv()

# ------------------ Pricing ------------------

LITELLM_URL = "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"
model_pricing_cache = {}
input_cost_per_token = 0.0
output_cost_per_token = 0.0


def fetch_model_pricing(model_name):
    global input_cost_per_token, output_cost_per_token
    if model_name in model_pricing_cache:
        input_cost_per_token, output_cost_per_token = model_pricing_cache[model_name]
        return
    try:
        r = requests.get(LITELLM_URL, timeout=5)
        if r.status_code == 200:
            data = r.json().get(model_name, {})
            input_cost_per_token = data.get("input_cost_per_token", 0.0)
            output_cost_per_token = data.get("output_cost_per_token", 0.0)
            model_pricing_cache[model_name] = (
                input_cost_per_token,
                output_cost_per_token,
            )
    except Exception:
        input_cost_per_token = output_cost_per_token = 0.0


def estimate_cost(token_info):
    pt = token_info.get("input_tokens", 0)
    rt = token_info.get("output_tokens", 0)
    return pt * input_cost_per_token + rt * output_cost_per_token, pt, rt


# ------------------ Dataset Loading ------------------

def load_dataset(dataset_file, eval_type):
    questions = []

    if eval_type == "seceval":
        with open(dataset_file, "r") as f:
            for q in json.load(f):
                questions.append({
                    "Question": q["question"],
                    "Choices": "\n".join(q["choices"]),
                    "Solution": q["answer"],
                })

    elif eval_type == "cybermetric":
        with open(dataset_file, "r") as f:
            data = json.load(f)
            for q in data.get("questions", []):
                questions.append({
                    "Question": q["question"],
                    "Choices": "\n".join(f"{k}: {v}" for k, v in q["answers"].items()),
                    "Solution": q["solution"],
                })

    elif eval_type == "cti_bench":
        with open(dataset_file, "r") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader, None)
            for row in reader:
                if len(row) >= 8:
                    questions.append({
                        "Question": row[1],
                        "Choices": f"A: {row[2]}\nB: {row[3]}\nC: {row[4]}\nD: {row[5]}",
                        "Solution": row[7],
                    })

    return questions


# ------------------ Model Call ------------------

def ask_model(question, instruction, model, api_base, api_key, provider, model_params=None):
    system_prompt = "You are a cybersecurity expert. Answer only with the correct letter choices."
    prompt = question["Question"] + "\n" + instruction
    if question["Choices"]:
        prompt += "\nChoices:\n" + question["Choices"]

    try:
        completion_kwargs = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "api_base": api_base,
            "api_key": api_key,
            "custom_llm_provider": provider,
        }
        
        # Add optional model parameters
        if model_params:
            if "temperature" in model_params and model_params["temperature"] is not None:
                completion_kwargs["temperature"] = model_params["temperature"]
            if "max_tokens" in model_params and model_params["max_tokens"] is not None:
                completion_kwargs["max_tokens"] = model_params["max_tokens"]
            if "top_p" in model_params and model_params["top_p"] is not None:
                completion_kwargs["top_p"] = model_params["top_p"]
            if "top_k" in model_params and model_params["top_k"] is not None:
                completion_kwargs["top_k"] = model_params["top_k"]
            if "frequency_penalty" in model_params and model_params["frequency_penalty"] is not None:
                completion_kwargs["frequency_penalty"] = model_params["frequency_penalty"]
            if "presence_penalty" in model_params and model_params["presence_penalty"] is not None:
                completion_kwargs["presence_penalty"] = model_params["presence_penalty"]
        
        resp = litellm.completion(**completion_kwargs)

        content = resp.choices[0].message.content
        usage = getattr(resp, "usage", None)

        token_info = {
            "input_tokens": getattr(usage, "prompt_tokens", 0),
            "output_tokens": getattr(usage, "completion_tokens", 0),
        } if usage else {}

        return content, token_info

    except Exception as e:
        print(f"[ERROR] {e}")
        return None, {}


# ------------------ MCQ Parsing ------------------

def parse_result_mcq(result):
    if not result:
        return None

    text = result.upper()

    # Prefer ANSWER: section if present
    m = re.search(r"ANSWER:?\s*([A-D,\s]+)", text)
    if m:
        text = m.group(1)

    letters = re.findall(r"[A-D]", text)
    return "".join(sorted(set(letters))) if letters else None


# ------------------ Accuracy ------------------

def compute_accuracy(results):
    correct = 0
    total = 0

    for r in results:
        sol = "".join(sorted(set(re.findall(r"[A-D]", r["Solution"].upper()))))
        pred = parse_result_mcq(r["ModelAnswer"])

        if pred is not None and pred == sol:
            correct += 1
        total += 1

    acc = (correct / total * 100) if total else 0.0
    return acc, correct, total


# ------------------ Runner ------------------

def format_time(seconds):
    """Format seconds into readable format (e.g., 1h 23m 45s)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"

def run_eval(dataset, instruction, model, api_base, api_key, provider, save_interval=None, status_interval=None, model_params=None):
    results = []
    total_cost = 0.0
    correct_count = 0
    wrong_count = 0
    start_time = time.time()
    last_status_time = start_time

    safe_model = "".join(c if c.isalnum() or c in "-_" else "_" for c in model)
    checkpoint_dir = os.path.join(os.getcwd(), "checkpoints", safe_model)
    os.makedirs(checkpoint_dir, exist_ok=True)
    
    total_questions = len(dataset)
    
    print(f"\n{'='*70}")
    print(f"Starting Evaluation")
    print(f"Model: {model}")
    print(f"Total questions: {total_questions}")
    if model_params:
        print(f"Model parameters: {', '.join(f'{k}={v}' for k, v in model_params.items() if v is not None)}")
    print(f"{'='*70}\n")

    for idx, q in enumerate(dataset, 1):
        answer, token_info = ask_model(q, instruction, model, api_base, api_key, provider, model_params)

        results.append({
            "Question": q["Question"],
            "Choices": q["Choices"],
            "ModelAnswer": answer,
            "Solution": q["Solution"],
        })

        # Track accuracy in real-time
        sol = "".join(sorted(set(re.findall(r"[A-D]", q["Solution"].upper()))))
        pred = parse_result_mcq(answer)
        if pred is not None and pred == sol:
            correct_count += 1
        else:
            wrong_count += 1

        cost, _, _ = estimate_cost(token_info)
        total_cost += cost

        # Print status at intervals
        current_time = time.time()
        elapsed = current_time - start_time
        
        if status_interval and (current_time - last_status_time) >= status_interval:
            accuracy = (correct_count / idx * 100) if idx > 0 else 0.0
            rate = idx / elapsed if elapsed > 0 else 0
            remaining = (total_questions - idx) / rate if rate > 0 else 0
            
            print(f"[{idx:4d}/{total_questions}] {idx/total_questions*100:5.1f}% | "
                  f"Correct: {correct_count:4d} | Wrong: {wrong_count:4d} | "
                  f"Accuracy: {accuracy:5.2f}% | Time: {format_time(elapsed)} | "
                  f"Est. remaining: {format_time(remaining)} | Cost: ${total_cost:.4f}")
            last_status_time = current_time

        if save_interval and idx % save_interval == 0:
            ckpt = os.path.join(checkpoint_dir, f"checkpoint_{idx}.json")
            with open(ckpt, "w") as f:
                json.dump(results, f, indent=2)

        if total_cost > 20:
            print("\n⚠️ Cost cap reached ($20) — stopping.")
            break

    print(f"\n{'='*70}")
    elapsed_total = time.time() - start_time
    print(f"Evaluation Completed")
    print(f"Questions: {idx}/{total_questions}")
    print(f"Correct: {correct_count} | Wrong: {wrong_count}")
    print(f"Total time: {format_time(elapsed_total)}")
    print(f"Total cost: ${total_cost:.4f}")
    print(f"{'='*70}\n")

    return results


# ------------------ CLI ------------------

def main():
    parser = argparse.ArgumentParser(description="Security Benchmark Evaluation for LLMs")
    parser.add_argument("-d", "--dataset_file", required=True, help="Path to dataset file")
    parser.add_argument("-e", "--eval", required=True, help="Evaluation type (seceval, cybermetric, cti_bench)")
    parser.add_argument("-B", "--backend", required=True, help="LLM backend (openai, anthropic, ollama, etc)")
    parser.add_argument("-m", "--model", required=True, help="Model name")
    parser.add_argument(
        "-s",
        "--save_interval",
        type=int,
        default=None,
        help="Save intermediate results every N questions",
    )
    parser.add_argument(
        "--status-interval",
        type=int,
        default=None,
        help="Print status update every N seconds (default: only at end)",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="Model temperature (0.0-2.0)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=None,
        help="Maximum tokens in response",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=None,
        help="Nucleus sampling parameter",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=None,
        help="Top-k sampling parameter",
    )
    parser.add_argument(
        "--frequency-penalty",
        type=float,
        default=None,
        help="Frequency penalty (-2.0 to 2.0)",
    )
    parser.add_argument(
        "--presence-penalty",
        type=float,
        default=None,
        help="Presence penalty (-2.0 to 2.0)",
    )
    args = parser.parse_args()

    fetch_model_pricing(args.model)

    backend = args.backend.upper()
    api_base = os.getenv(f"{backend}_API_BASE")
    api_key = None if args.backend == "ollama" else os.getenv(f"{backend}_API_KEY")
    provider = args.backend

    dataset = load_dataset(args.dataset_file, args.eval)

    instruction = (
        "Select ALL correct answers. Respond ONLY with letters A-D.\n"
        "Format: ANSWER: AC"
    )

    # Collect model parameters
    model_params = {
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "top_p": args.top_p,
        "top_k": args.top_k,
        "frequency_penalty": args.frequency_penalty,
        "presence_penalty": args.presence_penalty,
    }
    # Remove None values
    model_params = {k: v for k, v in model_params.items() if v is not None}

    results = run_eval(
        dataset,
        instruction,
        args.model,
        api_base,
        api_key,
        provider,
        args.save_interval,
        args.status_interval,
        model_params if model_params else None,
    )

    acc, correct, total = compute_accuracy(results)
    print(f"Final Accuracy: {acc:.2f}% ({correct}/{total})")

    safe_model = "".join(c if c.isalnum() or c in "-_" else "_" for c in args.model)
    out_file = f"benchmark_results_{args.eval}_{safe_model}.json"

    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to {out_file}")


if __name__ == "__main__":
    main()
