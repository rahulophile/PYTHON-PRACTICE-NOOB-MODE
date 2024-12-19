#WAP to print multiplication table of n using for loops in reverse order?

n = int(input("Enter the value of n : "))
for i in range(1,n+1) :
    print(f"{n} X {n+1-i} = {n * (n+1-i)}")