#Write a function count_vowels(s) that counts the number of vowels in a string.

'''def count_vowels(s):
    count = 0
    for i in range(0,len(s)) :
        if (s.lower()[i]=="a" or s.lower()[i]=="e" or s.lower()[i]=="i" or s.lower()[i]   =="o" or s.lower()[i]=="u") :
            count += 1
    print(f"There are {count} Vowels in '{s}'")

s = input("Enter your string : ")
count_vowels(s) ''' 

def count_vowels(s):
    count = 0
    vowels = "aeiou"
    s = s.lower()  # Convert the string to lowercase once
    for char in s:
        if char in vowels:
            count += 1
    print(f"There are {count} vowels in '{s}'")

s = input("Enter your string: ")
count_vowels(s)

#NOTE both are correct but lower one is more optimised.