# Convert an IPv4 address from dotted-decimal to binary format.
import ipaddress

ip = input("Enter an IPv4 address: ")

try:
    ipType = ipaddress.ip_address(ip)

    if ipType.version == 4:
        binary_parts = []

        for octet in ip.split('.'):
            binary_octet = f'{int(octet):08b}'
            binary_parts.append(binary_octet)

        print('.'.join(binary_parts))

    else:
        print("Please enter an IPv4 address.")

except ValueError:
    print("Invalid IP address.")
