import os
from datetime import datetime


def collect_file_timeline(path):
    print("\n=== File Timeline Evidence ===\n")

    for root, dirs, files in os.walk(path):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                stat = os.stat(filepath)

                created = datetime.fromtimestamp(stat.st_ctime)
                modified = datetime.fromtimestamp(stat.st_mtime)
                accessed = datetime.fromtimestamp(stat.st_atime)

                print(f"File: {filepath}")
                print(f"Created: {created}")
                print(f"Modified: {modified}")
                print(f"Accessed: {accessed}")
                print("-" * 60)

            except (PermissionError, FileNotFoundError):
                continue


if __name__ == "__main__":
    collect_file_timeline("evidence")
