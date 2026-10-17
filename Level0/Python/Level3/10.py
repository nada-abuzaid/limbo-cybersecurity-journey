# Given a dictionary of usernames and passwords, print the password for a given username.
credentials = {
    "alice": "password123",
    "bob": "securepass",
    "eve": "phising123"
}

input_username = input("Enter a username: ")
if input_username in credentials:
    print(f"The password for {input_username} is: {credentials[input_username]}")
else:
    print(f"Username {input_username} not found.")