#WAP to print following pattern for first n lines

# ***
# **
# * for n = 3

# n = int(input("Enter number of rows : "))

# for i in range(1,n+1) :
#     print("*" * (n+1-i) + " " * (i-1))

# lets solve this via recursion

def pattern(n):
        if (n==1) :
            return "*"
        else :
            print("*" * n)
            return pattern(n-1)
print(pattern(3))        