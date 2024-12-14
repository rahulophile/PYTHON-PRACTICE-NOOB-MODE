a = "I am Rahul Raj\nI am a good boy"
print(a)
print(a.replace("good", "bad"))

#\t gives space of a tab
b = "I am Rahul Raj\tI am a good boy"
print(b)

#between \"___\" the word will be print in "__" in a string
c = "I am Rahul Raj and I am a \"good\" boy" 
print(c)

#NOTE go on chatGPT and search for give me some escape sequence literals in string
#It would provide

# Escape sequences in action

print("1. Newline: Hello\nWorld")
print("2. Tab: Hello\tWorld")
print("3. Backslash: C:\\Users\\Rahul")
print('4. Single quote: It\'s a pen')
print('5. Double quote: She said, "Hello!"')
print("6. Carriage Return: Hello\rWorld")
print("7. Backspace: Hello\bWorld")
print("8. Form Feed: Hello\fWorld")
print("9. Vertical Tab: Hello\vWorld")
print("10. Null Character: Hello\0World")
print("11. Named Unicode (degree symbol): 30\N{degree sign}C")
print("12. 16-bit Unicode (degree symbol): \u00B0C")
print("13. 32-bit Unicode (emoji): \U0001F600")
print("14. Hexadecimal ASCII (A, B, C): \x41\x42\x43")


# Escape Sequence	Description	Example	Output
# \n	Newline (line break)	print("Hello\nWorld")	Hello
# World
# \t	Horizontal Tab (tab space)	print("Hello\tWorld")	Hello World
# \\	Backslash (\)	print("C:\\Users\\Rahul")	C:\Users\Rahul
# \'	Single quote (')	print('It\'s a pen')	It's a pen
# \"	Double quote (")	print("He said \"Hi\"")	He said "Hi"
# \r	Carriage return (moves to start of line)	print("Hello\rWorld")	World (overwrites 'Hello')
# \b	Backspace (removes previous character)	print("Hello\b World")	Hell World (removes 'o')
# \f	Form feed (page break)	print("Hello\fWorld")	Hello (form feed) World
# \v	Vertical tab (vertical space)	print("Hello\vWorld")	Hello (vertical space) World
# \0	Null character (used in C/C++)	print("Hello\0World")	Hello World (null is invisible)
# \N{name}	Unicode character by name	print("\N{degree sign}")	° (degree symbol)
# \uXXXX	Unicode character (16-bit)	print("\u00B0")	° (degree symbol)
# \UXXXXXXXX	Unicode character (32-bit)	print("\U0001F600")	😀 (grinning face emoji)
# \xXX	Hexadecimal character (ASCII)	print("\x41")	A (ASCII code for 'A' is 65)