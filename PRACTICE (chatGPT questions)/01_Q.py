#Create a function reverse_string(s) that takes a string and returns its reverse.

'''def reverse_string(s) :
    for i in range(0,len(s)) :
        print (s[len(s) - i -1], end='')
str = input("Enter your string : ")
reverse_string(str)'''

def reverse_string(s):
    reversed_str = ""  # Initialize an empty string to store the result
    for i in range(len(s) - 1, -1, -1):  # Iterate backward
        reversed_str += s[i]
    return reversed_str

str = input("Enter your string: ")
result = reverse_string(str)
print(f"Reversed string: {result}")


#NOTE both are correct but lower one is more optimised