# Convert a list into a comma-separated string.
items = ["apple", "banana", "cherry"]
comma_separated_string = ", ".join(str(item) for item in items)
print(comma_separated_string)