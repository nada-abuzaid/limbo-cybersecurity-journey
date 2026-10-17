# Store ports and services in a dictionary and allow user queries.
ports_and_services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    21: "FTP",
    25: "SMTP"
}

input_port = int(input("Enter a port number to look up the service: "))
if input_port in ports_and_services:
    print(f"Port {input_port} is used for {ports_and_services[input_port]}.")
else:
    print(f"Port {input_port} is not in the dictionary.")