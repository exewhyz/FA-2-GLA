
n = []
for i in range(1,10):
    n.append(i**2)
    
# print(n)

# [expression for value in iterable]
# print([i**2 for i in range(1,10)])

# [expression for value in iterable if condition]
# iterable - string, list, tuple, set

# print([value for value in range(1,10) if value % 2 == 0])

# [if_expression if condition else else_expression for value in iterable]

# print([ value * 2 if value % 2 == 0 else value *3 for value in range(1,10)])


names = ["aniket", "akash", "abhishek"]

# exp for value in iterable

# print([value.upper() for value in names])

# print([len(value) for value in names]) # list comprehension
# print({ value : value.upper() for value in names}) # dict comprehension
# print({ value.upper() for value in names}) # set comprehension


# [expression for i in iterable1 for j in iterable2 ]


print([ [i,j] for i in range(1,3) for j in range(2,5)])
print([ (i,j) for i in range(1,3) for j in range(2,5)])
print([ i+j for i in range(1,3) for j in range(2,5)])
print({ i : j for i in range(1,3) for j in range(2,5)}) # dict
print({ i + j for i in range(1,3) for j in range(2,5)}) # set


list1 = [1 , 2, 3]
list2 = ["one", "two", "three"]
list3 = ["I", "II", "III"]

# dict1 = {}
# for key,value in zip(list1,list2):
#     dict1[key] = value
print(list(zip(list1, list2,list3)))

# print({ key:value for key,value in zip(list1,list2) })