# set operations sem 2

# create and access set elements
set1 = {1, 2, 3, 4, 5}
print(set1)
for num in set1:
    print(num)

# union of elements
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9}
print(set1.union(set2))
# print(f"The union of the two sets is", {union})

# intersection of elements
int_set = set1.intersection(set2)
print(int_set)

# difference of sets
diff = set1-set2
print(diff)

