
# Extract IP Addresses from a Text File
import ipaddress
import re

with open('q3log.txt', 'r') as fh:
    lines = fh.readlines()

pattern = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
)

ip_list = []

for line in lines:
    result = re.findall(pattern, line)
    ip_list.extend(result)

for ip in ip_list:
    try:
        ipType = ipaddress.ip_address(ip)

        if ipType.version == 4:
            print(f"{ip} is a valid IPv4 address.")
        else:
            print(f"{ip} is not an IPv4 address.")

    except ValueError:
        print(f"{ip} is not a valid IP address.")