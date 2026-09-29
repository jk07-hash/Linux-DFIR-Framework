import subprocess


def collect_auth_logs():
    command = [
        "journalctl",
        "--no-pager",
        "-n",
        "50"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()

    print("\n=== Linux Authentication & Session Evidence ===\n")

    found = False

    for line in lines:
        if any(keyword in line.lower()
               for keyword in ["pam_unix", "authentication", "login", "session"]):
            print(line)
            found = True

    if not found:
        print("No authentication-related events found.")


if __name__ == "__main__":
    collect_auth_logs()
