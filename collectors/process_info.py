import psutil


def collect_processes():
    print("\n=== Running Process Evidence ===\n")

    for process in psutil.process_iter(
        ["pid", "name", "username", "create_time"]
    ):
        try:
            info = process.info
            print(
                f"PID: {info['pid']} | "
                f"Name: {info['name']} | "
                f"User: {info['username']} | "
                f"Created: {info['create_time']}"
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


if __name__ == "__main__":
    collect_processes()
