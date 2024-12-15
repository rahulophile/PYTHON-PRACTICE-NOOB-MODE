#chatGPT for it

marks = {
    "Rahul" : 100,
    "Aayat" : 80,
    "Zia" : 85,
    "Rohan" : 50,
    "list" : [12,23,44],
    0 : "Rahul"
}
print(marks[0])
print(marks.items())
print(marks.keys())
print(marks.values())



marks = {
    "Rahul" : 100,
    "Aayat" : 80,
    "Zia" : 85,
    "Rohan" : 50,
    "list" : [12, 23, 44],
    0 : "Rahul"
}

# 1. Get the value of 'Rahul'
print(marks.get("Rahul"))  # 100

# 2. Get all keys
print(marks.keys())  # dict_keys(['Rahul', 'Aayat', 'Zia', 'Rohan', 'list', 0])

# 3. Get all values
print(marks.values())  # dict_values([100, 80, 85, 50, [12, 23, 44], 'Rahul'])

# 4. Get all items
print(marks.items())  # dict_items([('Rahul', 100), ('Aayat', 80), ('Zia', 85), ('Rohan', 50), ('list', [12, 23, 44]), (0, 'Rahul')])

# 5. Update 'marks' with a new key-value pair and add one
marks.update({"Rahul" : 99, "Aman": 75})
print(marks)  # {'Rahul': 99, 'Aayat': 80, 'Zia': 85, 'Rohan': 50, 'list': [12, 23, 44], 0: 'Rahul', 'Aman': 75}

# 6. Remove 'Rohan' and return its value
print(marks.pop("Rohan"))  # 50

# 7. Remove the last item from the dictionary
print(marks.popitem())  # (0, 'Rahul')

# 8. Create a copy of the dictionary
copy_marks = marks.copy()
print(copy_marks)  # {'Rahul': 100, 'Aayat': 80, 'Zia': 85, 'list': [12, 23, 44]}

# 9. Create a new dictionary using fromkeys()
new_dict = dict.fromkeys(["X", "Y", "Z"], 0)
print(new_dict)  # {'X': 0, 'Y': 0, 'Z': 0}

# 10. Check if 'Rahul' is a key in the dictionary
print('Rahul' in marks)  # True

# 11. Get the number of items in the dictionary
print(len(marks))  # 4



#NOTE : Difference btwn dic.get("element") & dict["element"]


print(marks.get("Rahul2")) #returns none
print(marks["Rahul2"]) #returns error