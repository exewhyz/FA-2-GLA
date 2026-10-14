# numbers = [ 1, 4, 2, 1, 5, 6, 8,3, 3, 4, 1]

# sets = set() # empty set

# print(list(set(numbers)))


data = { "a", "b", "a", "c", "b" }
# for value in data:
#     print(value)

data.add("d")
# data.update(["e", "f"])
# data.update(("e", "f"))
# data.update({"e", "f"})
data.update("hello")
# data.remove("z")
data.discard("z")
# print("removed value:",data.pop())
# data.clear()

# print(data)

# print("d" in data)


"""
set operations
1. union
2. intersection
3. difference
4. symmetric diff
5. isDisjoint
"""
set_A = {1, 5, 9, 2, 4, 10, 6}
set_B = {2, 4}
set_C = {15}

# print(set_A | set_B | set_C)
# print(set_A.union(set_B).union(set_C))

# print(set_A & set_B | set_C)
# print(set_A.intersection(set_B).union(set_C))

# print(set_A - set_B - set_C)
# print(set_A.difference(set_B).difference(set_C))

# print(set_A.issubset(set_B))
# print(set_B.issubset(set_A))
# print(set_A.issuperset(set_B))
# print(set_A.issubset(set_A))
# print(set_A.isdisjoint(set_C))

print(set_A >= set_B)
print(set_B <= set_A)


x = frozenset({1,2,3,4,5})
print(x)