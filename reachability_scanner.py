import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2
        )
        return host if result.returncode == 0 else None
    except subprocess.TimeoutExpired:
        return None


def get_ip_range():
    user_input = input("Enter IP range (e.g. 192.168.0.1-100): ").strip()

    try:
        base, rng = user_input.rsplit(".", 1)
        start, end = map(int, rng.split("-"))

        if not (0 < start <= end <= 255):
            raise ValueError

        return base + ".", start, end

    except Exception:
        print("Invalid format. Example: 192.168.0.1-100")
        exit(1)


def main():
    try:
        network, start, end = get_ip_range()
        ips = [f"{network}{i}" for i in range(start, end + 1)]

        print("\nReachable hosts")
        print("-" * 30)

        reachable = []

        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(ping, ip) for ip in ips]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    reachable.append(result)
                    print(result)

        print("\nSummary")
        print("-" * 30)
        print(f"Total reachable: {len(reachable)}")

    except KeyboardInterrupt:
        print("\n\nScan cancelled by user.")
        print("Exiting cleanly.")



if __name__ == "__main__":
    main()
