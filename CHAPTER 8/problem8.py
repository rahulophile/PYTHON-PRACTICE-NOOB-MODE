#WAP to print multiplication table of a given number

def multiplication(n):
    for i in range(1,11):
        print (f"{n} X {i} = {n*i}")

multiplication(9)