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
# print(n)
#1,2,"Aniket",3
n.pop(-2)
# print(n)

d = [1,2,3,2,4,2]
d.remove(2)
# print(d)

# CREATE
# append(value) -> add value at the end
# insert(index, value) -> add value at the given index

# DELETE
# pop(index = -1) -> remove value at the given index
# remove(value) -> remove first matched value
# del items[index] -> keyword

first_index = 0 or -len(items)
last_index = -1 or len(items) - 1


it = [1,2,3,4,3,5,6,3,2]
# print(it.count(4)) #count(value) -> return count of given value

#index(value, start = 0, stop = len(list))
# print(it.index(2,-2))
# print(it.index(3,0,6))


l = [1,2,3]

# reverse() -> reverse the list
# l.reverse()
# print(l)

# l.sort()
# print(l)

# x = [64,45,52,5,8,99,2]
# x.sort(reverse=True)
# print(x)

# y = ["t","D","a","A","T"]
# y.sort(reverse=True)
# print(y)

names = ["Shivang","Aniket", "Pulkit","Aakash", "Mayank", "Riddhi"]
# names.sort(key=len, reverse=True)
# print(names)

# z = [-562, -203, 197, 436, -170, -64]

# z.sort(key=abs)
# print(z)

# abs(-10) #10

b = [3,2,4,1,6,5]

def aniket(abs):
    # print(abs % 2 ==0 and abs + 1)
    if(abs % 2 == 0):
        return abs + 1
    else:
        return abs

new_list = sorted(b, key=aniket)
print("old list", b)
print("normal",sorted(b))
print("New List", new_list)
