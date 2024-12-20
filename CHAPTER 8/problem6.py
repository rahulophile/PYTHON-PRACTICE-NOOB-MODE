# WAP which converts inches to centimeters

def inchToCenti(inch) :
    return inch * 2.54

inch = int(input("Enter the value of inche/inches : "))
print(f"{inch} Inches = {inchToCenti(inch)} Centimeters")