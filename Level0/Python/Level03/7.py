# Function to remove duplicates from a list.
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]

def remove_duplicates(input_list):
    unique_items = []
    for item in input_list:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

print(remove_duplicates(list_with_duplicates))