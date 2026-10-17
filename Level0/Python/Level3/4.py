# Count how many times each letter appears in a string.
input_string = input("Enter a string: ").lower()
letter_count = {}
for char in input_string:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
print(letter_count)