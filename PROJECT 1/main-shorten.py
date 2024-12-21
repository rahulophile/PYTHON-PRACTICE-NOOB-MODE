import random #this package help select random number 
computer = random.choice([1, -1, 0])
youstr = input("Enter s for, w for water, g for gun : ")
youDict = {"s" : 1,"w" : -1,"g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youstr]
print(f"Computer Choosen : {reverseDict[computer]}")
print(f"You Choosen : {reverseDict[you]}")

if(computer == you) :
    print("It's a Draw!!")
else :
    if ((computer - you) == -1  or (computer - you) == 2):
        print("You Lose!")
    else :
        print("You Win!!")     


#NOTE this is also a way to make snake water game but it is not readable        