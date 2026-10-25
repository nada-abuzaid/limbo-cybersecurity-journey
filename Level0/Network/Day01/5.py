# Given an IP and subnet mask, calculate the network address and broadcast address.
import ipaddress

ip = input("Enter an IP address: ")
subnet_mask = input("Enter a subnet mask: ")

try:
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)

    network_address = network.network_address
    broadcast_address = network.broadcast_address

    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")

except ValueError as e:
    print(f"Error: {e}")