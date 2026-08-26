items = ["Oil", "Wheat", "Sugar", "Rice", 100, True, 3.14, 3 + 4j]
# print(type(items))
# print(len(items))

last_index = len(items)-1

#CRUD

# Read
# print(items[2])

# Create
items.append(200)
# print(items)

# items[10] = "Milk"
# print("new",items)

# Update
items[0] = "Tea"
# print("updated", items)
# Delete
del items[1]
# print("deleted", items)


n = [1,2,3]

n.insert(2, "Aniket")
print(n)
#1,2,"Aniket",3
n.pop(-2)
# print(n)

d = [1,2,3,2,4,2]
d.remove(2)
print(d)