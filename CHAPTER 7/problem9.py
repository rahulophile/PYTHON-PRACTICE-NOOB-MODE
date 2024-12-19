#WAP to print the following pattern
# ***
# * *
# *** for n = 3 and so on

n = int(input("Enter the value of n : "))
for i in range (1,n+1) :
    if(i==1 or i==n) :
        print("*" * n)
    else :
        print("*" + " " *(n-2) + "*")    