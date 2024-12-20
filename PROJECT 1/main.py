#JAB BHI HAM EK PROJECT BANATE HAI TO FILE KO main.py se banate hai

'''
1 : for snake
-1 : for water
0 : for gun
'''

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
    if(computer==-1 and you==1):
        print("You Win!!")
    elif(computer==-1 and you==0):
        print("You Lose!!")    
    elif(computer==1 and you==-1):
        print("You Lose!!") 
    elif(computer==1 and you==0):
        print("You Win!!")
    elif(computer==0 and you==-1):
        print("You Win!!") 
    elif(computer==0 and you==1):
        print("You Lose!!")
    else:
        print("Something Went Wrong!!")                 