# Create a script that checks if an IP is reachable by pinging it.
import ipaddress
import subprocess

ip = input("Enter an IP address: ")

try:
    ip_obj = ipaddress.ip_address(ip)

    result = subprocess.run(
        ["ping", "-c", "4", str(ip_obj)],
        capture_output=True,
        text=True,
        timeout=10
    )

    if result.returncode == 0:
        print(f"{ip} is reachable.")
    else:
        print(f"{ip} did not respond to ping.")

except ValueError:
    print("Invalid IP address.")

except subprocess.TimeoutExpired:
    print("Ping timed out.")