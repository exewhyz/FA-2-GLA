# Challenge A — Bill
# Price = 1000, quantity = 2, discount = 10%. Find the final price.

price = 1000
quantity = 2
discount = 10

total = price * quantity
discount_amount = total * discount / 100
final_price = total - discount_amount

print(final_price)  # 1800.0

# Challenge B — Last digit
# How can you get the last digit of 1234?

num = 1234
last_digit = num % 10
print(last_digit)  # 4

# Challenge C — Student eligibility
# A student must be at least 18 and have marks ≥ 60. Write the Boolean expression.
age = 19
marks = 78
age >= 18 and marks >= 60