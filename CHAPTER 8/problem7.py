#WAP to remove a given word from a list and strip it at the same time

def remove(l, word):
    n = []
    for item in l:
        if not(item == word) :
            n.append(item.strip(word)) # strip will remove a/n/an from starting and begining
    return n

l=["Rahul", "Pandey", "Rohan", "Saumya", "Pratikn", "an"]
print(remove(l, "an"))
