import argparse
import json
import os
import subprocess
import sys
from typing import Any, Dict


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_mapping() -> Dict[str, Dict[str, Any]]:
    mapping_path = os.path.join(PROJECT_ROOT, "data", "testcase_mapping.json")
    with open(mapping_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_pytest_for_method(method_name: str, env: str, browser: str) -> int:
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-k",
        method_name,
        f"--env={env}",
        f"--browser={browser}",
        "--maxfail=1",
    ]
    return subprocess.call(cmd, cwd=PROJECT_ROOT)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run pytest based on TC_ID mapping.")
    parser.add_argument("--TC_ID", required=True, help="Test case ID (e.g., TC_LOGIN_001)")
    parser.add_argument("--env", default="qa", help="Pytest --env option (qa/prod)")
    parser.add_argument("--browser", default="chrome", help="Pytest --browser option")
    args = parser.parse_args()

    mapping = load_mapping()

    tc = args.TC_ID.strip()
    if tc not in mapping:
        available = ", ".join(sorted(mapping.keys()))
        raise SystemExit(f"Unknown TC_ID: {tc}. Available TC_IDs: {available}")

    method_name = mapping[tc].get("method")
    objective = mapping[tc].get("objective", "")

    if not isinstance(method_name, str) or not method_name:
        raise SystemExit(f"Invalid mapping for {tc}: missing/empty 'method'")

    print(f"[detecttest] TC_ID={tc}")
    if objective:
        print(f"[detecttest] objective={objective}")
    print(f"[detecttest] Running pytest method: {method_name}")

    exit_code = run_pytest_for_method(
        method_name=method_name,
        env=args.env,
        browser=args.browser,
    )

    if exit_code == 0:
        print(f"[detecttest] TC_ID={tc} => PASS")
    else:
        print(f"[detecttest] TC_ID={tc} => FAIL (exit code {exit_code})")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
