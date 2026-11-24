
import json
from pathlib import Path
from template2 import build_template2

ROOT = Path(__file__).resolve().parent.parent

# Existing reference cases from Member C
cases_path = ROOT / "T1_test_cases_reference.json"

with open(cases_path, "r", encoding="utf-8-sig") as f:
    test_cases = json.load(f)

for case_name, case_data in test_cases.items():

    prompt = build_template2(case_data)

    print("=" * 70)
    print(case_name)
    print(f"Booking ID: {case_data['row_id']}")
    print(prompt)
