# Generate a list of all possible IPs in a given subnet.
import ipaddress

subnet = input("Enter a subnet (e.g., 192.168.1.0/24): ")

try:
    network = ipaddress.ip_network(subnet, strict=False)

    ip_list = [str(ip) for ip in network.hosts()]
    print(f"Total IP addresses: {len(ip_list)}")

    for ip in ip_list:
        print(ip)

except ValueError:
    print("Invalid subnet.")