# name = input()
# print("Entered name is",name)

# name= input("Enter your name ")
# age = input("Enter your age ")

# print(type(age))
# print(int(age) == 15)
# print("Name:",name,"\n","Age:",age)

# print(1, end="and")
# print(2)

# print("Your name","aniket",sep=1)

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# print(num1 + num2) # string concatenation -> "10" + "20" = "1020"
# print(int(num1) + int(num2))

# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# area = length * width
# print("Area of rectangle is",area)

# b , h = input("Enter value of base and height:").split(" ")  #"5 6" -> ["5", "6"]
# print("Area of triangle is:", 1/2*int(b)*int(h))

# b,h = map(int, input("Enter value of base and height:").split(" ")) #"5 6" -> ["5", "6"] -> [5,6]
# print("Area of triangle is:", 1/2*b*h)


quantity = int(input("Enter number of products to add in stock: "))
price = float(input("Enter the price of product: "))

total = quantity * price
# print("Total Income", total)
print(f"Total Income {total:.1f}")