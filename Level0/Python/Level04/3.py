# Generate a random password of 12 characters.
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

def generate_random_password(length=12):
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

print(generate_random_password())