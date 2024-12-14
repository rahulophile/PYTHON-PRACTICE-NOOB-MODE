#TUPLE : A tuple is an ordered, immutable collection of items in Python. Tuples are similar to lists, but unlike lists, tuples cannot be modified (no adding, deleting, or changing elements) after they are created.

a = (1,4.5,"Darling",False)
print(a)

no = a.count(1)
print(no)

b = (1,) #way to create single element tuple
c = () #way to create empty tuple
print(b,c)