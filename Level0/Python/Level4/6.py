# Generate random MAC addresses.
import random
import string

def generate_random_mac():
    mac = [
        random.choice(string.hexdigits).upper() +
        random.choice(string.hexdigits).upper() for _ in range(6)]
    return ":".join(mac)

print(generate_random_mac())