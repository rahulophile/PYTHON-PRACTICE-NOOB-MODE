#WAP to find whether given number is prime or not?

n = int(input("Enter the number : "))
# count = 0;
# if (n > 1) :
#     for i in range(1, n+1) :
#         if(n%i == 0) :
#             count +=1
# else :
#     print("You have entered 1 or a negative number.")
# if(count == 2) :
#     print("It is a Prime Number")
# else :
#     print("It is not a Prime Number")       


#THIS IS MORE EFFICIENT CODE THAN IPPER ONE
for i in range(2,n) :
    if(n%i == 0):
        print("Number is not Prime")
        break
else :
    print("Number is Prime")    