import os
import re
import pandas as pd

# Extract step and perplexity values from the log
def extract_ppl_from_log(filepath):
    results = {}
    current_step = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            step_match = re.search(r"Step:\s*(\d+)", line)
            if step_match:
                current_step = int(step_match.group(1))
            ppl_match = re.search(r"ppl:\s*([\d.]+)", line)
            if ppl_match and current_step:
                results[current_step] = float(ppl_match.group(1))
                current_step = None
    return results

logs = {
    "Baseline": "../logs/deen_transformer_regular/baseline",
    "Prenorm": "../logs/deen_transformer_pre/pre",
    "Postnorm": "../logs/deen_transformer_post/post"
}

data = {model: extract_ppl_from_log(path) for model, path in logs.items()}

all_steps = sorted(set().union(*[d.keys() for d in data.values()]))

with open("../validation_ppl_table.md", "w", encoding="utf-8") as f:
    f.write("| Validation ppl | Baseline | Prenorm | Postnorm |\n")
    f.write("|-----------------|----------|---------|----------|\n")
    for step in all_steps:
        row = [str(step)]
        for model in ["Baseline", "Prenorm", "Postnorm"]:
            val = data[model].get(step, "")
            row.append(f"{val:.2f}" if isinstance(val, float) else "")
        f.write(f"| {' | '.join(row)} |\n")