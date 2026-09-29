from pathlib import Path
from datetime import datetime


EVIDENCE_DIR = Path("evidence")


def analyze_evidence():
    print("\n=== DFIR Evidence Correlation Engine ===\n")

    files = list(EVIDENCE_DIR.glob("*.txt"))

    if not files:
        print("No evidence files found.")
        return

    print(f"Evidence files found: {len(files)}\n")

    for file in files:
        stat = file.stat()

        created = datetime.fromtimestamp(stat.st_ctime)
        modified = datetime.fromtimestamp(stat.st_mtime)

        print(f"Evidence: {file.name}")
        print(f"Created : {created}")
        print(f"Modified: {modified}")
        print("-" * 60)


if __name__ == "__main__":
    analyze_evidence()
