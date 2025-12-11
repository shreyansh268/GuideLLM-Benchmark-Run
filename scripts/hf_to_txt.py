#!/usr/bin/env python3
"""
hf_to_txt.py
------------
Utility script to download a Hugging Face dataset and export prompts to a .txt file
for use with GuideLLM benchmarking.

Usage:
    python hf_to_txt.py --dataset tatsu-lab/alpaca --split train --field instruction --output alpaca_prompts.txt

Arguments:
    --dataset   Hugging Face dataset ID (e.g., "tatsu-lab/alpaca")
    --split     Dataset split to use (default: "train")
    --field     Field/column name containing the prompt text (default: "instruction")
    --output    Output .txt file path (default: "prompts.txt")
"""

import argparse
from datasets import load_dataset

def main():
    parser = argparse.ArgumentParser(description="Convert HF dataset to .txt for GuideLLM")
    parser.add_argument("--dataset", required=True, help="Hugging Face dataset ID")
    parser.add_argument("--split", default="train", help="Dataset split (default: train)")
    parser.add_argument("--field", default="instruction", help="Field containing prompt text")
    parser.add_argument("--output", default="prompts.txt", help="Output .txt file")
    args = parser.parse_args()

    # Load dataset
    print(f"📥 Loading dataset: {args.dataset} [{args.split}]")
    ds = load_dataset(args.dataset, split=args.split)

    # Write prompts to file
    with open(args.output, "w", encoding="utf-8") as f:
        for row in ds:
            if args.field in row and row[args.field]:
                f.write(row[args.field].strip() + "\n")

    print(f"✅ Exported {len(ds)} prompts to {args.output}")

if __name__ == "__main__":
    main()