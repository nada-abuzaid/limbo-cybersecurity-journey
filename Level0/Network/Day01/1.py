# Write a Python script that validates whether a given IP address is IPv4 or IPv6.
import ipaddress

def is_valid_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.version
    except ValueError:
        return None

ip = input("Enter an IP address: ")
result = is_valid_ip(ip)

if result == 4:
    print(f"{ip} is a valid IPv4 address.")
elif result == 6:
    print(f"{ip} is a valid IPv6 address.")
else:
    print(f"{ip} is not a valid IP address.")