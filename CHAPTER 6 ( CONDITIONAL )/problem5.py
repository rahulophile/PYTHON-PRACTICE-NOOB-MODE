#WAP which finds out finds out whether a given name is present in a list or not.

name = ["Pandey","Pranav", "Dipu", "Aniket", "Prem", "Bittu", "Harsh"]
newname = input("Enter your name : ")
if(newname in name) :
    print("You are in the list!")
else :
    print("You are not in the list!")