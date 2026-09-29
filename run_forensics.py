import subprocess

print("=" * 69)
print("        LINUX DIGITAL FORENSIC FRAMEWORK")
print("=" * 69)

modules = [
    "collectors/system_info.py",
    "collectors/auth_logs.py",
    "collectors/process_info.py",
    "collectors/network_info.py",
    "collectors/file_timeline.py",
]

for module in modules:
    print(f"\n[+] Running: {module}")
    subprocess.run(["python3", module])

print("\n[+] Running anomaly detector")
subprocess.run(["python3", "analyzer/anomaly_detector.py"])

print("\n[+] Generating forensic report")
subprocess.run(["python3", "analyzer/report_generator.py"])

print("\n" + "=" * 69)
print("        FORENSIC INVESTIGATION COMPLETED")
print("=" * 69)
