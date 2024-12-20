#WAP to print following pattern for first n lines

# ***
# **
# * for n = 3

# n = int(input("Enter number of rows : "))

# for i in range(1,n+1) :
#     print("*" * (n+1-i) + " " * (i-1))

# lets solve this via recursion

def pattern(n):
        if (n==0) :
            return  #sirf return likhne ka mtlb ab aage nahi chalega yahi se baher ho jao
        else :
            print("*" * n)
            return pattern(n-1)
pattern(3)        