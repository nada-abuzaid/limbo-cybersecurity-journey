# Check if an IP address is valid.
ip = input("Enter an IP address: ")
parts = ip.split(".")
if len(parts) == 4:
    valid = True
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            valid = False
            break
    if valid:
        print(f"{ip} is a valid IP address.")
    else:
        print(f"{ip} is not a valid IP address.")
else:
    print(f"{ip} is not a valid IP address.")