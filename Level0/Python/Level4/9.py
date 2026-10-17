# Resolve a hostname to an IP address.
import socket

hostname = input("Enter a hostname: ")
ip_address = socket.gethostbyname(hostname)

print("IP address:", ip_address)