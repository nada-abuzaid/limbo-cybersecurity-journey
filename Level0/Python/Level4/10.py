# Extract all vowels from a string
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char in vowels:
        result += char

print("Vowels:", result)