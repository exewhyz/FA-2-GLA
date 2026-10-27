# try:
    # statement
# except exception_name1, exception_name2, ...:
    # statement
# except exception_name1, exception_name2, ...:
    # statement
# except:
    # statement


# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
# except ValueError as error:
#     print("Invalid Input:", error)
# except ZeroDivisionError as error:
#     print("Cannot divide by zero:", error)
# else:
#     print(result)
# finally:
#     print("Done")

# try:
#     print(1 + "1")
# except TypeError as e:
#     print("Error:", e)
# except Exception as e:
#     print(e)


def divide(a, b):
    return a / b

def calculate():
    return divide(10, 0)

try:
    calculate()
except ZeroDivisionError:
    print("Cannot divide by zero")