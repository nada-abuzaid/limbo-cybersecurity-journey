# Check if a password is strong (≥8 chars, includes number & special character).
def check_password_strength(password):
    if len(password) < 8:
        return False

    has_number = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_number = True

        elif not char.isalnum():
            has_special = True

    return has_number and has_special

print(check_password_strength("Password1!"))