#Write a function remove_duplicates(lst) that takes a list of integers and returns a new list with duplicates removed while preserving the original order.

def remove_duplicates(lst):
    i =0
    while(i<len(lst)):
        count = 0
        for j in range (0, len(lst)):
            if lst[j] in lst:
                count +=1
            if(count ==2):
                lst.remove(lst[j])  
        i +=1          
    print(lst)


lst1 = [1,2,3,3,3,3,4]
remove_duplicates(lst1)                