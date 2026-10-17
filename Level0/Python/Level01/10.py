# Replace all vowels in "P@ssw0rd" with "*".
text = "P@ssw0rd"
result = ""

for char in text:
    if char.lower() in "aeiou":
        result += "*"
    else:
        result += char

print(result)