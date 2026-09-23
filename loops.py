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

# y = [1,2,3,4,5,6]
# index = 5
# while index >= 0:
#     print(y[index])
#     index = index - 1

# b = 3
# while b < 2:
#     print(b)
#     b += 1

# break keyword => stops the execution of loop

# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# continue keyword => skips that execution

# for i in range(1,5):
#     if i % 2 == 0:
#         print("skiping value",i)
#         continue
#     print(i)
    
# pass keyword => 

# print("continue:")
# for i in range(1,6):
    
#     if i == 4:
#         continue
#     print(i)
# print("-"*20)
# print("Pass:")  
# for i in range(1,6):
#     if i == 4:
#         pass
#     print(i)

# find total after multiplying 1 to 100 numbers
# find factorial

# total = 1
# number = int(input("Enter the number: "))
# for num in range(1, number + 1):
#     total = total * num
# print(total)

# Searching implementation

# movies = ("Dhurandhar", "Spiderman", "It", "Nun", "Thor", "Titanic")

# search_text = input("Enter movie name: ").strip().lower()

# for mov in movies:
#     if search_text in mov.lower():
#         print("Movie Found:", mov)
#         break
# else:
#     print(f"{search_text} not available")

# Nested Loops

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)
#     print("-" * 20)
    

# for i in range(1,5):
#     for j in range(4,0,-1):
#         print(i,j)
#     print("-" * 20)

# for i in range(1,6):
#     print(i * "*")

# for i in range(1,6):
#     for j in range(1,i+1):
#         if j == 1 or j == i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         # print("*",end="")
#     print("")


# for i in range(1,6):
#     print(str(i) * i)


# for _ in range(5):
#     for _ in range(5):
#         print("*",end=" ")
#     print()

# vowels = "aeiou"

# text = input("Enter your text: ").strip().lower()

# count = 0

# for ch in text:
#     if ch in vowels.lower():
#         count += 1

# print(count)

# count of digits in a string

# total_digits = 0

# txt = "hello12hello3"

# for ch in txt:
#     if ch.isdigit():
#         total_digits += 1
        
# print(total_digits)


# Count how many marks are greater than or equal to 75 using a loop and conditional statement.

marks = [78, 65, 89, 92, 56, 71]




# check a number is prime or not

# num = int(input("Enter a number: "))
# for num in range(1,101):
#     if num < 2:
#         # print(num,"Not Prime")
#         pass
#     else:
#         is_prime = True
#         for v in range(2,num):
#             if num % v == 0:
#                 is_prime = False
#         if is_prime:
#             print(num)
#         # else:
#         #     print(num,"Not Prime")
    
    

134

# 1 ** 3 + 3 ** 3 + 4 ** 3 = 125

# x = 153

# total = 0

# while x > 0:
#     last_digit = x % 10
#     total = total + last_digit ** 3
#     x = x // 10
# if total == x:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

x = 153
total = 0
for ch in str(x):
    total = total + int(ch) ** 3
    
if total == x:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
