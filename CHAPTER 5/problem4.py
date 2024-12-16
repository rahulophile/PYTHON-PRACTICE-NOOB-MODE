# What will be the length of the following set
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
print(s)

#NOTE : python returns true for {1==1.0}