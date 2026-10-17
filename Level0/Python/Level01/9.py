# Print "H4ck3r" with alternating uppercase and lowercase letters.
text = "H4ck3r"
count = 0

for char in text:
    if char.isalpha():
        if count % 2 == 0:
            print(char.lower(), end="")
        else:
            print(char.upper(), end="")
        count += 1
    else:
        print(char, end="")