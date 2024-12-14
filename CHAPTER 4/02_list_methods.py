#NOTE : the major difference btwn String Methods and List Methods, string method gives new string and does not change original string but List methods manipulate original list and provide us manipulated changed LIST.

container = ["Apple", "Orange", 0, 12.4, False, "Aayat", "Sai Pallavi"]
container[1] = 1
print(container)
container.append("Nayantara")
print(container) #this will add extra element in the lst of list

numbers = [1,2,40,5,8,19,23,30,80]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(8)
print(numbers)
numbers.insert(3,100)
print(numbers)
numbers.pop(1) #will delete elmnt at index 2 and return its value
print(numbers)
numbers.remove(23) #will delete 40 from the list
print(numbers)

#Now search 'give me most useful list methods in python'

fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'orange']

fruits = ['apple', 'banana']
fruits.extend(['grape', 'mango'])
print(fruits)  # Output: ['apple', 'banana', 'grape', 'mango']

numbers = [1, 2, 4, 5]
numbers.insert(2, 3)  # Insert 3 at index 2
print(numbers)  # Output: [1, 2, 3, 4, 5]

fruits = ['apple', 'banana', 'apple', 'mango']
fruits.remove('apple')  # Removes the first occurrence of 'apple'
print(fruits)  # Output: ['banana', 'apple', 'mango']

fruits = ['apple', 'banana', 'mango']
fruits.pop()  # Removes the last element
print(fruits)  # Output: ['apple', 'banana']

fruits.pop(0)  # Removes the element at index 0
print(fruits)  # Output: ['banana']

fruits = ['apple', 'banana', 'mango']
fruits.clear()
print(fruits)  # Output: []

fruits = ['apple', 'banana', 'mango']
index = fruits.index('banana')
print(index)  # Output: 1

fruits = ['apple', 'banana', 'apple', 'mango', 'apple']
count = fruits.count('apple')
print(count)  # Output: 3

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Sort in descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 2, 1, 1]

fruits = ['apple', 'banana', 'mango']
fruits.reverse()
print(fruits)  # Output: ['mango', 'banana', 'apple']

fruits = ['apple', 'banana', 'mango']
copy_fruits = fruits.copy()
print(copy_fruits)  # Output: ['apple', 'banana', 'mango']

fruits = ['apple', 'banana', 'mango']
print(len(fruits))  # Output: 3

numbers = [1, 4, 9, 2, 7]
print(max(numbers))  # Output: 9

numbers = [1, 4, 9, 2, 7]
print(min(numbers))  # Output: 1

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

# Convert string to list of characters
letters = list('hello')
print(letters)  # Output: ['h', 'e', 'l', 'l', 'o']

# Convert tuple to list
tup = (1, 2, 3)
print(list(tup))  # Output: [1, 2, 3]

fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

names = ['John', 'Alice', 'Bob']
scores = [90, 85, 88]

combined = list(zip(names, scores))
print(combined)  # Output: [('John', 90), ('Alice', 85), ('Bob', 88)]

