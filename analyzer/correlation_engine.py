from pathlib import Path
from datetime import datetime

EVIDENCE_DIR = Path("evidence")


def get_file_time(file):
    stat = file.stat()
    return datetime.fromtimestamp(stat.st_mtime)


def analyze_evidence():
    print("\n=== DFIR Evidence Correlation Engine ===\n")

    files = list(EVIDENCE_DIR.glob("*.txt"))

    if not files:
        print("No evidence files found.")
        return

    evidence = []

    for file in files:
        modified = get_file_time(file)

        evidence.append({
            "name": file.name,
            "modified": modified
        })

    evidence.sort(key=lambda x: x["modified"])

    print("=== Evidence Timeline ===\n")

    for item in evidence:
        print(
            f"{item['modified']}  ->  {item['name']}"
        )

    print("\n=== Correlation Complete ===")


if __name__ == "__main__":
    analyze_evidence()
