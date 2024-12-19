'''
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

factorial(n) = n X n-1 X n-2 ..... X 3 X 2 X 1
factorial(n) = n * factorial(n-1)
factorial(p) = p * p-1 * factorial(p-2) 
'''

def factorial(n) :
    if(n==0 or n==1) :
        return 1
    else :
        return n * factorial(n-1)

n = int(input("Enter the number : "))
print(f"Factorial of {n} = {factorial(n)}")    


#NOTE the programmers needs to be extreme careful and must include base condition where recursion exits otherwise it may go into infinite loop