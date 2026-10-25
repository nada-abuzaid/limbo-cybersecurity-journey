# Convert an IPv6 address to its compressed and expanded forms.
import ipaddress

ip = input("Enter an IPv6 address: ")

try:
    ip_obj = ipaddress.IPv6Address(ip)

    print(f"Compressed format: {ip_obj.compressed}")
    print(f"Expanded format: {ip_obj.exploded}")

except ValueError:
    print("Invalid IPv6 address.")