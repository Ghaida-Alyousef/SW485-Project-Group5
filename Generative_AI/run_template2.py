
import os
import json
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from template2 import TEMPLATE_VERSION, build_template2

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "Generative_AI" / "example_outputs" / f"T2_v{TEMPLATE_VERSION}"

load_dotenv(ROOT / ".env")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

# Use the same model as Member C where available.
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

if OUTPUT_DIR.exists():
    raise SystemExit("The versioned output folder already exists.")

client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=30000))


def request(operation, stage):
    try:
        return operation()
    except Exception as error:
        # SDK error details can contain request information.
        raise SystemExit(f"Gemini {stage} failed ({type(error).__name__}).") from None


request(lambda: client.models.get(model=MODEL), "model lookup")

with open(
    ROOT / "T1_test_cases_reference.json",
    encoding="utf-8-sig"
) as file:
    test_cases = json.load(file)

results = []
case_reports = {}

for case_number, (case_name, case) in enumerate(
    test_cases.items(), start=1
):
    prompt = build_template2(case)

    print(f"\nRunning Template 2: {case_name}")

    start = time.perf_counter()

    response = request(lambda: client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=2048,
            thinking_config=types.ThinkingConfig(
                thinking_level="minimal"
            ),
        ),
    ), "generation")

    elapsed = round(time.perf_counter() - start, 2)
    output = response.text or ""

    if not output.strip():
        raise RuntimeError(
            f"No text returned for {case_name}"
        )

    record = {
        "template_id": "T2",
        "template_version": TEMPLATE_VERSION,
        "case": case_name,
        "row_id": case["row_id"],
        "model": MODEL,
        "prompt": prompt,
        "response": output,
        "word_count": len(output.split()),
        "response_seconds": elapsed,
    }

    results.append(record)

    case_reports[f"T2_case{case_number}.md"] = (
        f"# Template 2 - {case_name}\n\n"
        f"## Prompt\n\n{prompt}\n\n"
        f"## Response\n\n{output}\n"
    )

    print(f"Words: {record['word_count']}")
    print(f"Time: {elapsed} seconds")

    # Small delay between API requests
    if case_number < len(test_cases):
        time.sleep(5)

client.close()
OUTPUT_DIR.mkdir()
for filename, report in case_reports.items():
    (OUTPUT_DIR / filename).write_text(report, encoding="utf-8")

results_file = OUTPUT_DIR / "T2_results.json"
results_file.write_text(
    json.dumps(results, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

print("\nTemplate 2 testing completed.")
print(f"Results saved to: {results_file}")
