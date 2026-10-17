# Simulate a login system that locks after 3 failed attempts.
failed_attempts = 0
password = "secret"

while failed_attempts < 3:
    entered_password = input("Enter the password: ")
    if entered_password == password:
        print("Access granted.")
        break
    else:
        failed_attempts += 1
        print(f"Access denied. Attempt {failed_attempts}/3.")