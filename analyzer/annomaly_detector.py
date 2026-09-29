from pathlib import Path

EVIDENCE_DIR = Path("evidence")

KEYWORDS = [
    "failed",
    "failure",
    "denied",
    "invalid",
    "unauthorized"
]

print("=== DFIR Suspicious Activity Detector ===")
print("Scanning evidence files...\n")

found = False

for file in EVIDENCE_DIR.glob("*.txt"):
    try:
        lines = file.read_text(errors="ignore").splitlines()

        for number, line in enumerate(lines, 1):
            for keyword in KEYWORDS:
                if keyword in line.lower():
                    print(
                        f"[ALERT] {file.name} | "
                        f"Line {number} | "
                        f"Keyword: {keyword}"
                    )
                    found = True
                    break

    except OSError:
        continue

if not found:
    print("No suspicious activity detected.")
