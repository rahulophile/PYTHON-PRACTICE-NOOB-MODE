# Write a recursive function to calculate the sum of first n natural  umbers

def sum(n):
    if(n==1):
        return 1
    else :
        return (sum(n-1) + n)

print(sum(3))