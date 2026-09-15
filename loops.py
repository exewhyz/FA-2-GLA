# Loop Works on List,Tuple,String

# Type of loops
# 1. for loop
# 2. while loop

text = "Python Programming"
# print(text.upper())
# EVEN INDEX chars (P,t,o," ",r,g,a,m,n)

# for value in text:
#     print(value)


# nums= [1,2,3,4,5]
# for num in nums:
#     print(num)
    
    

"""
SYNTAX

for value_name in str/list/tuple_name:
    #logic
"""

# n = [54, 6, 9, 3, 2]

# for value in n:
#     if value % 2 == 0:
#         print(value,"is Even")
#     else:
#         print(value, "is odd")


# len()
# type()
# print()
# input()
# sum()
# max()
# min()
# abs()
# int()
# float()
# complex()
# str()
# sorted()


# range(start,stop,step) -> int

# print(range(6))
# print(list(range(6)))
# print(list(range(2,6)))
# print(type(range(6)))

# for i in range(11):
#     print(i)
    
# for value in range(1,101):
#     value % 2 == 0 and print(value)

# for value in range(2,101,2):
#     print(value)
    
# for ch in "hello":
#     print(ch)
    
# write a program to check if student got less than 50 marks in any of the subjects.

# marks = [70, 49, 74, 80, 50]
# marks = map(int, input("Enter your mnarks: ").split())

# for mark in marks:
#     if mark >= 50:
#         print("pass")
#     else:
#         print("fail")

# for i in range(4,-1,-1):
#     print(i)


# max 
# nums = [70, 49, 74, 80, 50]

# if len(nums) > 0:
#     maximum = nums[0]
#     for n in nums:
#         if n > maximum:
#             maximum = n
#     print(maximum)
# else:
#     print("List is empty")
    
# min 
# nums = [70, 49, 74, 80, 50]

# if len(nums) > 0:
#     minimum = nums[0]
#     for n in nums:
#         if n < minimum:
#             minimum = n
#     print(minimum)
# else:
#     print("List is empty")

# sum([nums],start=0)

# prices = [70, 49, 74, 80, 50]
# start = 0
# for amt in prices:
#     start = start + amt

# print(start)


# find the count of even numbers from a list

# numbers = [70, 49, 71, 80, 50]
# count = 0

# for n in numbers:
#     if n % 2 == 0:
#         count = count + 1

# print(count)

# search and print the index

# x = [1,2,3,4,5]
# search = int(input("Enter your number for search: "))
# found = False

# for val in x:
#     if search == val:
#         found = f"Value found at index {x.index(val)}" 

# print(found)


# while loop

# while True:
#     print("you are hacked")


# start = 1
# while start <= 5:
#     print(start)
#     start = start + 1

# y = [1,2,3,4,5,6]
# index = 2
# while index < len(y):
#     print(y[index])
#     index = index ** 2

y = [1,2,3,4,5,6]
index = 5
while index >= 0:
    print(y[index])
    index = index - 1