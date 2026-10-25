# Write a Python script that validates whether a given IP address is IPv4 or IPv6.
import ipaddress

def is_valid_ip(ip):
    try:
        ipType = ipaddress.ip_address(ip)
        if ipType.version == 4:
            print(f"{ip} is a valid IPv4 address.")
        elif ipType.version == 6:
            print(f"{ip} is a valid IPv6 address.")
    except ValueError:
        print(f"{ip} is not a valid IP address.")

ip = input("Enter an IP address: ")
is_valid_ip(ip)