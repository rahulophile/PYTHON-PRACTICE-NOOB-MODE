#WAP to accept marks of 6 students & display them in a sorted manner

a = []
s1 = int(input("Enter marks of student 1 : "))
a.append(s1)
s2 = int(input("Enter marks of student 2 : "))
a.append(s2)
s3 = int(input("Enter marks of student 3 : "))
a.append(s3)
s4 = int(input("Enter marks of student 4 : "))
a.append(s4)
s5 = int(input("Enter marks of student 5 : "))
a.append(s5)
s6 = int(input("Enter marks of student 6 : "))
a.append(s6)

a.sort()
print(a)
