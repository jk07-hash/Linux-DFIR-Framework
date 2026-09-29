from pathlib import Path
from datetime import datetime

EVIDENCE_DIR = Path("evidence")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)

report_file = REPORT_DIR / "forensic_report.txt"

with report_file.open("w") as report:

    report.write("DFIR FORENSIC INVESTIGATION REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write(f"Report Generated: {datetime.now()}\n")
    report.write("Case Type: Linux Digital Forensic Investigation\n\n")

    report.write("EVIDENCE FILES\n")
    report.write("-" * 50 + "\n")

    for file in sorted(EVIDENCE_DIR.glob("*.txt")):
        report.write(f"- {file.name}\n")

    report.write("\nINVESTIGATION STATUS\n")
    report.write("-" * 50 + "\n")
    report.write("Evidence collection completed.\n")
    report.write("Initial analysis completed.\n")
    report.write("Further investigation may be required.\n")

print(f"Report created: {report_file}")
