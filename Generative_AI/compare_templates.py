
import argparse
import json
import re
from pathlib import Path

import pandas as pd
import textstat

ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "example_outputs"

def load_results(filename):
    with open(OUTPUTS / filename, encoding="utf-8") as f:
        return json.load(f)

parser = argparse.ArgumentParser(description="Compare saved Gemini responses.")
parser.add_argument("--t2-results", default="T2_results.json", help="Path relative to example_outputs")
parser.add_argument("--include-revised", action="store_true", help="Include T2 v1.1 beside the archived baselines")
parser.add_argument("--output", type=Path, help="Optional path to a new CSV")
parser.add_argument("--summary-output", type=Path, help="Optional path to a new averages CSV")
args = parser.parse_args()

t1 = load_results("T1_results.json")
t2 = load_results(args.t2_results)

# Domain-specific vocabulary, defined before evaluation.
keywords = [
    "booking", "completion", "probability",
    "segment", "passenger", "route",
    "risk", "recommendation", "conversion",
    "action", "customer", "flight"
]

def keyword_alignment(text):
    words = set(re.findall(r"[a-z]+", text.lower()))
    matches = [word for word in keywords if word in words]
    return round(100 * len(matches) / len(keywords), 2)

def evaluate(record):
    response = record["response"]

    return {
        "case": record["case"],
        "row_id": record["row_id"],
        "template": "T2 v1.1" if record.get("template_version") == "1.1" else record["template_id"],
        "model": record["model"],
        "word_count": len(response.split()),
        "keyword_alignment_pct": keyword_alignment(response),
        "flesch_kincaid_grade":
            round(textstat.flesch_kincaid_grade(response), 2),
    }

result_sets = [t1, t2]
if args.include_revised:
    if args.t2_results != "T2_results.json":
        parser.error("--include-revised requires the original T2 baseline")
    result_sets.append(load_results("T2_v1.1/T2_results.json"))

# Ensure every result set contains one response per shared case.
expected = {(x["row_id"], x["case"]) for x in t1}
for results in result_sets:
    if len(results) != len(expected) or {(x["row_id"], x["case"]) for x in results} != expected:
        raise ValueError("Test cases do not match!")

records = [evaluate(record) for results in result_sets for record in results]
df = pd.DataFrame(records)

print("\nCOMPARISON RESULTS")
print(df.to_string(index=False))

print("\nAVERAGE METRICS")
summary = df.groupby("template")[
        ["word_count", "keyword_alignment_pct",
         "flesch_kincaid_grade"]
].mean().round(2)
print(summary)

if args.output:
    df.to_csv(args.output, index=False, mode="x")
if args.summary_output:
    summary.to_csv(args.summary_output, mode="x")
