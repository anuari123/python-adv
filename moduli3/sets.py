my_set = {1,2,3,3}
print(my_set)

my_set = set([1,2,3,3])
print(my_set)

set1 = {1,2,3}
set2 = {3,4,5}

union_result_method = set1.union(set2)
print(union_result_method)

#intersection
intersection_result_method = set1.intersection(set2)
print(intersection_result_method)


#difference
difference_method = set1.difference(set2)
difference_operator = set1.difference(set2)
print(difference_operator)
print(difference_method)

#simetric
symmetric_difference = set1.symmetric_difference(set2)
symmetric_difference_operator = set1.symmetric_difference(set2)
print(symmetric_difference_operator)
print(symmetric_difference)

my_set = {1,2,3}
my_set.add(7)
print(my_set)
my_set.remove(7)
print(my_set)

my_set.discard(8)
print(my_set)

my_set.clear()
print(my_set)

#in operator
colors = {"red","green","blue"}
color = "green"
print(color in colors)
print(color not in colors)

3