"""
1. Module - collection of variables, functions, class, expressions or statements
2. Package - collection of modules
3. Library - collection of packages
"""

"""
types of module

1. Built-in module
2. Third-party module
3. User-defined/custom module
"""

# import random
# import os
# import math
# import calendar

# print(calendar.isleap(2026))
# print(random.random())
# print(random.randint(1,10))
# print(math.factorial(5))

# import calculator
# calculator.add(3,4)
# calculator.sub(4,2)
# print(calculator.PI)

# from calculator import PI,sub
# sub(4,1)
# print(p)

# from calculator import PI as p,sub
# sub(4,1)
# print(p)

# from calculator import *
# add(4,3)
# sub(7,3)
# print(PI)

# import calculator as calc

# print("before import")
# import calculator
# print("Running entry.py statements...")

# import calculator 

# from users import getuser
# getuser.getusername()

from users.getuser import getusername
getusername()

import users.getuser
users.getuser.getusername()