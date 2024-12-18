#WAP to find factorial of given number using for loop
n = int(input("Enter a number : "))
i = 1
fact = 1
while(i<=n):
    fact = fact*i
    i += 1
print(f"Factorial of {n} = {fact}")    