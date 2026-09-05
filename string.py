

greeting = "Hello Aniket"
greeting = "hii piyush"

# print(len(greeting))
# print(greeting[4])

# greeting[4] = "P" #not possible to update str object

# del greeting[6] #not possible to delete chars of str object

# print(greeting[0::2])

a = "how"
b = "are"
c = "you"
d = a + " " + b + " " + c
# print(d)

# print(a * 5)

# z = "" or '' or """""" or ''''''

# print(len(z))

# print("-" * 20)

text = "Python Programming"
# print("Python  " not in text)
# text[0] = "p" # wrong
# text = "p" + text[1:] # "p" + "ython Programming" => "python Programming"


"""
String Methods => string_name.method_name()

1. lower()
2. upper()
3. capitalize()
4. title()
5. swapcase()
6. strip()
7. lstrip()
8. rstrip()
9. replace()
10. find()
11. count()
12. index()
13. startswith()
14. endswith()
15. split()
16. join()
17. isdigit()
18. isalpha()
19. isalnum()
20. isspace()
"""

p = "PYTHON"
print("LOWERCASE:", p.lower())

q = "python pRogramming"
print("UPPERCASE:", q.upper())
print("CAPITALIZE:", q.capitalize())

greet = "    !!!!11111heLlo, HOW aRe yOu?####"
print("TITLE:", greet.title())
print("SWAPCASE:", greet.swapcase())
print("STRIP:", greet.strip(" 1!#"))
# print("LEFT STRIP:", greet.lstrip(), end="@\n")
# print("RIGHT STRIP:", greet.rstrip(),end="@\n")