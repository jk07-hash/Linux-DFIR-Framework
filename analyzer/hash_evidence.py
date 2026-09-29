import hashlib
from pathlib import Path

EVIDENCE_DIR = Path("evidence")


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with file_path.open("rb") as file:
        for block in iter(lambda: file.read(4097), b""):
            sha256.update(block)

    return sha256.hexdigest()


print("=== Evidence Integrity Verification ===\n")

for file in sorted(EVIDENCE_DIR.glob("*.txt")):
    file_hash = calculate_sha256(file)

    print(f"Evidence: {file.name}")
    print(f"SHA-256: {file_hash}")
    print("-" * 70)
