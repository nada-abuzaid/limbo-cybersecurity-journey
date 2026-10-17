# Write a script that asks for a password and only allows access if it matches "s3cr3t".
password = input("Enter the password: ")
if password == "s3cr3t":
    print("Access granted.")
else:
    print("Access denied.")