my_tuple = (10, 20, 20, 30, 40, 50, 10, 60)

# 1. count() - Count occurrences of 20 in the tuple
count_of_20 = my_tuple.count(20)
print("Count of 20:", count_of_20)  # Output: 2

# 2. index() - Find the index of the first occurrence of 30 in the tuple
index_of_30 = my_tuple.index(30)
print("Index of 30:", index_of_30)  # Output: 3

# 3. len() - Get the length of the tuple
length = len(my_tuple)
print("Length of tuple:", length)  # Output: 8

# 4. max() - Find the maximum value in the tuple
maximum_value = max(my_tuple)
print("Maximum value:", maximum_value)  # Output: 60

# 5. min() - Find the minimum value in the tuple
minimum_value = min(my_tuple)
print("Minimum value:", minimum_value)  # Output: 10

# 6. sum() - Calculate the sum of all the elements in the tuple
sum_of_elements = sum(my_tuple)
print("Sum of elements:", sum_of_elements)  # Output: 240

# 7. sorted() - Return a sorted list from the tuple
sorted_tuple = sorted(my_tuple)
print("Sorted tuple (as list):", sorted_tuple)  # Output: [10, 10, 20, 20, 30, 40, 50, 60]

# 8. tuple() - Convert a list to a tuple
my_list = [100, 200, 300]
converted_tuple = tuple(my_list)
print("Converted tuple from list:", converted_tuple)  # Output: (100, 200, 300)

# 9. in operator - Check if 40 is in the tuple
is_40_present = 40 in my_tuple
print("Is 40 present in tuple:", is_40_present)  # Output: True

# 10. + operator - Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# 11. * operator - Repeat the tuple 3 times
repeated_tuple = tuple1 * 3
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# 12. Tuple slicing - Extract elements from index 2 to 5 (inclusive of 2, exclusive of 6)
sliced_tuple = my_tuple[2:6]
print("Sliced tuple (index 2 to 5):", sliced_tuple)  # Output: (20, 30, 40, 50)

# 13. enumerate() - Enumerate through the tuple and print index, value pairs
print("Enumerate the tuple:")
for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")

# 14. zip() - Combine two tuples into a list of pairs
names = ("Alice", "Bob", "Charlie")
scores = (90, 85, 88)
zipped_list = list(zip(names, scores))
print("Zipped list of names and scores:", zipped_list)  # Output: [('Alice', 90), ('Bob', 85), ('Charlie', 88)]
