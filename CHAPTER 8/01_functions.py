#Function Defination
def average() :
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = int(input("Enter third number : "))
    d = int(input("Enter fourth number : "))
    average = (a+b+c+d)/2
    # print("Average : ", average)
    return average

a = average() #Function Call
print(a)
print("Thank You!")
average() #Again Function Call