# Sort a list of random numbers without using .sort().
list_of_numbers = [5, 2, 9, 1, 5, 6]
sorted_list = []

while list_of_numbers:
    min_value = min(list_of_numbers)
    sorted_list.append(min_value)
    list_of_numbers.remove(min_value)
print(sorted_list)