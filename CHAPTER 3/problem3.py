#WAP to detect double space in string and then correct it with single space
string = "Hello brother! How  are you?"
print(string.find("  "))

print(string.replace("  ", " "))

#If output have a non negative integer then double space detected

#NOTE that string are immutable that means if we manipulate it with any fucntion