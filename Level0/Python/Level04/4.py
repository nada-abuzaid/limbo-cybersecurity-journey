# Create an MD5 hash of a user-entered string using hashlib.
import hashlib
entered_string = input("Enter a string to hash: ")
hashed_string = hashlib.md5(entered_string.encode()).hexdigest()

print(f"MD5 hash of '{entered_string}' is: {hashed_string}")