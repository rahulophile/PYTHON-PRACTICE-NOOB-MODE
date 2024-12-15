s = {1,2,3,4,4,4,4,5,8, "Rahul"}
print(s, type(s))

#Methods of set
# Initialize the set
s = {1, 2, 3, 4, 5, 8, "Rahul"}

# 1. add(element)
s.add(10)
print("After add(10):", s)  # {1, 2, 3, 4, 5, 8, 10, 'Rahul'}

# 2. remove(element)
s.remove(2)
print("After remove(2):", s)  # {1, 3, 4, 5, 8, 10, 'Rahul'}

# 3. discard(element)
s.discard(8)
s.discard(100)  # No error if element is not found
print("After discard(8) and discard(100):", s)  # {1, 3, 4, 5, 10, 'Rahul'}

# 4. pop()
popped_element = s.pop()
print("Popped element:", popped_element)
print("After pop():", s)  # Random element removed

# 5. clear()
s_copy = s.copy()  # To keep a copy for future examples
s.clear()
print("After clear():", s)  # set()

# 6. copy()
s = s_copy.copy()
print("Copy of set:", s)  # Restores the set {3, 4, 5, 10, 'Rahul'}

# 7. union(other_set)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
union_set = s1.union(s2)
print("Union of s1 and s2:", union_set)  # {1, 2, 3, 4, 5}

# 8. update(other_set)
s1.update(s2)
print("After update(s2) to s1:", s1)  # {1, 2, 3, 4, 5}

# 9. intersection(other_set)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
intersection_set = s1.intersection(s2)
print("Intersection of s1 and s2:", intersection_set)  # {3, 4}

# 10. intersection_update(other_set)
s1.intersection_update(s2)
print("After intersection_update(s2) to s1:", s1)  # {3, 4}

# 11. difference(other_set)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
difference_set = s1.difference(s2)
print("Difference of s1 - s2:", difference_set)  # {1, 2}

# 12. difference_update(other_set)
s1.difference_update(s2)
print("After difference_update(s2) to s1:", s1)  # {1, 2}

# 13. symmetric_difference(other_set)
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
symmetric_diff_set = s1.symmetric_difference(s2)
print("Symmetric difference of s1 and s2:", symmetric_diff_set)  # {1, 2, 5, 6}

# 14. symmetric_difference_update(other_set)
s1.symmetric_difference_update(s2)
print("After symmetric_difference_update(s2) to s1:", s1)  # {1, 2, 5, 6}

# 15. isdisjoint(other_set)
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print("Is s1 disjoint with s2?", s1.isdisjoint(s2))  # True

s3 = {3, 4, 5}
print("Is s1 disjoint with s3?", s1.isdisjoint(s3))  # False

# 16. issubset(other_set)
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print("Is s1 a subset of s2?", s1.issubset(s2))  # True

s3 = {1, 5}
print("Is s3 a subset of s2?", s3.issubset(s2))  # False

# 17. issuperset(other_set)
s1 = {1, 2, 3, 4}
s2 = {1, 2}
print("Is s1 a superset of s2?", s1.issuperset(s2))  # True

s3 = {5, 6}
print("Is s1 a superset of s3?", s1.issuperset(s3))  # False

# 18. len(set)
s = {1, 2, 3, 4, 5, 8, "Rahul"}
print("Length of set s:", len(s))  # 7

# 19. in Operator
print("Is 4 in set s?", 4 in s)  # True
print("Is 100 in set s?", 100 in s)  # False
