
# Check if an IP address is private
import ipaddress

ip = input("Enter an IP address: ")

def is_private_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return None

result = is_private_ip(ip)

if result is None:
    print(f"{ip} is not a valid IP address.")
elif result:
    print(f"{ip} is a private IP address.")
else:
    print(f"{ip} is not a private IP address.")