import psutil


def collect_network_info():
    print("\n=== Network Interface Evidence ===\n")

    interfaces = psutil.net_if_addrs()

    for interface, addresses in interfaces.items():
        print(f"\nInterface: {interface}")

        for address in addresses:
            print(f"  Family: {address.family}")
            print(f"  Address: {address.address}")
            print(f"  Netmask: {address.netmask}")


if __name__ == "__main__":
    collect_network_info()
