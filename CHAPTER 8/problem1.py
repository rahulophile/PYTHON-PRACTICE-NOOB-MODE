#WAP using function to find greatest of three number 

def greatest(x,y,z) :
    if(x==y==z):
        print("All numbers are equal")
    else :
        if(x > y and x > z):
            return x
        elif(y > x and y > z) :

            return y
        else :
            return z
        

n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))

print(f"{greatest(n1,n2,n3)} is the greatest number.")
