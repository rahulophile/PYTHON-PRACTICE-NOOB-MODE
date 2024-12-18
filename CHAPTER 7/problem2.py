#WAP to greet all the person names stored in a list 'l' and which start with S.

l = ["Rahul", "Pranav", "Aman", "Sonam", "Sonali", "Soaham", "Piyush"]

#SOLVED BY ME
# for i in range(0, len(l)) :
#     if("R".lower() in l[i][0].lower()) :
#         print(f"Good morning {l[i]}")

#SOLVED BY HARRY BHAYA
for name in l :
    if(name.startswith("S")) :
        print(f"Hello {name}")