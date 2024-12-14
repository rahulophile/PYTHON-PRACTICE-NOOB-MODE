name = "rahul raj" 
print(len(name))
print(name.endswith("aj"))
print(name.startswith("Ra"))
print(name.capitalize())

#NOTE : search ("give me most used string function in pyhton on chatGpt");
# After searching we get

# Sample string for demonstration
name = "rahul raj"

# 1. Basic Operations
print("1. Length of the string:")
print(len(name))  # Output: 9 (Total characters including spaces)

print("\n2. Check if string ends with 'aj':")
print(name.endswith("aj"))  # Output: True (The string ends with 'aj')

print("\n3. Check if string starts with 'Ra':")
print(name.startswith("Ra"))  # Output: False (Because 'R' is lowercase here)

print("\n4. Capitalize the first letter of the string:")
print(name.capitalize())  # Output: 'Rahul raj' (First character is capitalized)

# 2. String Case Conversions
print("\n5. Convert to uppercase:")
print(name.upper())  # Output: 'RAHUL RAJ'

print("\n6. Convert to lowercase:")
print(name.lower())  # Output: 'rahul raj'

print("\n7. Title case (capitalize first letter of each word):")
print(name.title())  # Output: 'Rahul Raj'

# 3. String Trimming
print("\n8. Remove whitespace from both sides:")
print(name.strip())  # No extra whitespace to remove in this case

print("\n9. Remove whitespace from the left:")
print(name.lstrip())  # No extra whitespace to remove in this case

print("\n10. Remove whitespace from the right:")
print(name.rstrip())  # No extra whitespace to remove in this case

# 4. Searching in Strings
print("\n11. Find the position of 'raj':")
print(name.find("raj"))  # Output: 6 (Index of where 'raj' starts)

print("\n12. Count occurrences of 'ra':")
print(name.count("ra"))  # Output: 2 (Both 'rahul' and 'raj' contain 'ra')

print("\n13. Check if string contains only alphabets:")
print(name.isalpha())  # Output: False (because of the space in 'rahul raj')

print("\n14. Check if string contains only digits:")
print(name.isdigit())  # Output: False (because it contains letters)

# 5. Replacing and Splitting
print("\n15. Replace 'raj' with 'kumar':")
print(name.replace("raj", "kumar"))  # Output: 'rahul kumar'

print("\n16. Split the string into a list using space as a delimiter:")
print(name.split())  # Output: ['rahul', 'raj']

# 6. Joining Strings
print("\n17. Join list of words with a hyphen '-':")
print("-".join(['rahul', 'raj']))  # Output: 'rahul-raj'

# 7. Character Classification
print("\n18. Check if all characters are alphanumeric (letters or numbers, no spaces):")
print(name.isalnum())  # Output: False (because of the space)

print("\n19. Check if all characters are uppercase:")
print(name.isupper())  # Output: False (because all letters are lowercase)

print("\n20. Check if all characters are lowercase:")
print(name.islower())  # Output: True (all letters are lowercase)

print("\n21. Check if all characters are whitespace:")
print("   ".isspace())  # Output: True (Only whitespace in the string)

print("\n22. Check if string follows title case:")
print(name.istitle())  # Output: False (because 'rahul' and 'raj' are not capitalized)

# 8. String Alignment
print("\n23. Center the string within 20 characters, filled with '*':")
print(name.center(20, '*'))  # Output: '*****rahul raj*****'

print("\n24. Left-justify the string within 20 characters, filled with '*':")
print(name.ljust(20, '*'))  # Output: 'rahul raj***********'

print("\n25. Right-justify the string within 20 characters, filled with '*':")
print(name.rjust(20, '*'))  # Output: '***********rahul raj'

# 9. String Formatting
print("\n26. Format a string using .format() method:")
print("Hello, {}!".format(name))  # Output: 'Hello, rahul raj!'

print("\n27. Use f-string to format a string:")
print(f"Hello, {name}!")  # Output: 'Hello, rahul raj!'

# 10. Padding with Zeros
print("\n28. Pad the string '42' with leading zeros to make it 5 characters long:")
print("42".zfill(5))  # Output: '00042'

# 11. Partition and Splitlines
print("\n29. Partition the string using a space as a delimiter:")
print(name.partition(" "))  # Output: ('rahul', ' ', 'raj')

print("\n30. Split the string into lines (useful for multi-line strings):")
multi_line_string = "Hello\nWorld\nPython"
print(multi_line_string.splitlines())  # Output: ['Hello', 'World', 'Python']
