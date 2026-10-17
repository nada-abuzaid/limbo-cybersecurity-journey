# Continuously ask for a password until the correct one is entered.
password = ""

while password != "secret":
    password = input("Enter the password: ")

print("Access granted.")