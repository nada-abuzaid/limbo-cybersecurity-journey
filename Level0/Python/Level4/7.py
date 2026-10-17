# XOR encryption function.
def xor_encrypt(text, key):
    encrypted = ""

    for c in text:
        encrypted_char = chr(ord(c) ^ ord(key))
        encrypted += encrypted_char

    return encrypted


text = input("Enter text: ")
key = input("Enter a single character key: ")

encrypted_text = xor_encrypt(text, key)
print("Encrypted text:", encrypted_text)