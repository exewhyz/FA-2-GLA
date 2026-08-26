# if 15 > 14:
#     print("Hello")
# else:
#     print("bye")
    
"""
SYNTAX

if condition:
    logic
else:
    logic
"""
# if True:
#     print("hej")
#     print("hej")

# print("hej")
# print("hej")
# print("hej")

# a = int(input("enter your age: "))

# if a > 18:
#     print("You can drive")
# else:
#     print("You can't drive")   


#else if ladder
# marks = float(input("Enter your marks: "))

# if marks < 34:
#     print("you are fail")
# elif marks >= 34 and marks < 50:
#     print("Grade D")
# elif marks >= 50 and marks < 60:
#     print("Grade C")
# elif marks >= 60 and marks < 70:
#     print("Grade B")
# elif marks >= 70 and marks < 80:
#     print("Grade A")
# elif marks >= 80 and marks < 90:
#     print("Grade A+")
# elif marks >= 90 and marks <= 100:
#     print("Grade S")
# else:
#     print("Enter marks within the range of 0 to 100")
    




# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator symbol: ")

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# else:
#     print("Enter valid operator symbol")
    
# match/switch case

# choice = "abc"

# match choice:  
#     case True:
#         print("true")
#     case False:
#         print("false")
#     case _:
#         print("default case")
        


# match "hello":
#     case "hii":
#         print("hii")
#     case "hello":
#         print("hello")
#     case _:
#         print("Invalid case")

# marks = 60
# match marks:
#     case marks if marks < 34:
#         print("fail")
#     case marks if marks >= 34 and marks < 50:
#         print("D")


print("""
      1. Create an user
      2. Read all users data
      3. Update user data
      4. Delete user data
      5. Exit the program
""")
choice = int(input("Enter your choice for operation: "))

match choice:
    case 1:
        print("Create an user")
    case 2:
        print("Read all users data")
    case 3:
        print("Update user data")
    case 4:
        print("Delete user data")
    case 5:
        print("Exit the program")
    case _:
        print("Invalid choice")
        
