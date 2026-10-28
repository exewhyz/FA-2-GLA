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

# try:
#     calculate()
# except ZeroDivisionError:
#     print("Cannot divide by zero")
    
    
# raise TypeError("Custom error message")
# raise Exception("Custom error message")
# raise
# raise ValueError

# try:
#     raise Exception("Custom Error")
# except Exception as e:
#     print("Error handled:",e)

# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise TypeError("Age can't be negative")
#     print(age)
# except TypeError as e:
#     print("Error:", e)
# except Exception as e:
#     print("Other Error:", e)
    
# class InsufficientBalanceError(Exception):
#     pass
    
# def withdraw(balance, amount):

#     if amount > balance:
#         raise InsufficientBalanceError("Insufficient balance")

#     return balance - amount

# try:
#     print("Balance Left:",withdraw(100, 110))
# except Exception as e:
#     print("Error:", e)


class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount

# try:
#     balance = 5000
#     amount = int(input("Enter withdrawal amount: "))
#     balance = withdraw(balance, amount)
# except ValueError as e:
#     print("Invalid amount:", e)
# except InsufficientBalanceError as e:
#     print("Transaction failed:", e)
# else:
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)
# finally:
#     print("Thank you for using our banking system")
    
    
try:
    age = int(input("Enter your age: "))
    # if age < 0:
    #     raise ValueError("Age must be postive")
    assert age >= 0, "Age must be Postive"
except Exception as e:
    print("Error:",e)