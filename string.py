

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
# print("LOWERCASE:", p.lower())

q = "python pRogramming"
# print("UPPERCASE:", q.upper())
# print("CAPITALIZE:", q.capitalize())

greet = "    !!!!11111heLlo, HOW aRe yOu?####"
# print("TITLE:", greet.title())
# print("SWAPCASE:", greet.swapcase())
# print("STRIP:", greet.strip(" 1!#"))
# print("LEFT STRIP:", greet.lstrip(), end="@\n")
# print("RIGHT STRIP:", greet.rstrip(),end="@\n")


# replace(old,new) -> str

o = "I like Java"
# print("Replaced:",o.replace("Java", "Python"))

# find(value,start=0,end=len(str)) -> int

# -1 => if value is not present in range
# 0 to len(str)-1 => value is present in range

# print(o.find("like"))

g = "hello hello hello bye"
# print("COUNT:", g.count("hello",6))

#startswith(value,start=0,end=len(str)) -> bool
#endswith(value,start=0,end=len(str)) -> bool
# value can be str or (str,str,str,....)

msg = "hello world"

# print(msg.startswith("l", 2,8))
# print(msg.endswith(("hello", "world"),2,8))


# split(sep=None,maxsplit=-1) -> list[str]
message = "a-b-c-d-e"

# print(message.split("-",maxsplit=3))


email = "test@gmail.com" # username and domain separated by '@'

username, domain = email.split("@")

# print(username)
# print(domain)

# str -> list  => split()
# list -> str => join()

full_name = ["Aniket", "Raj"]

# print("@".join(full_name))


# e = ["ankit", "gla", ".in"]
# username = e[0]
# domain = e[1:]
# full_dom = "".join(domain)
# full_email = [username,full_dom]
# # email_add = username+"@"+domain
# email_add = "@".join(full_email)
# print(email_add)


# str.isdigit() -> bool => "56257"
# str.isalpha() -> bool => "fsyajgdk"
# str.isalnum() -> bool => "vfd638dftshy"
# str.isspace() -> bool => "      "

g = "56257"
# print(g.isdigit())
h="fsyajgdk"
# print(g.isalpha())
h="vfd638dftshy"
# print(g.isalnum())
h="      "
# print(g.isspace())

# take username as input and check it should be at least 3 chars.

# username = input("Enter username: ")

# if len(username) >= 3:
#     print("Username is valid.✅")
# else:
#     print("Provide at least 3 characters.❌")

#string comaprision
# print("1" == "2")

#check the string is like email or not

# email = input("enter your email: ")
# #hello@gla.in

# if "@" in email and "." in email:
#     print("It is like an email")
# else:
#     print("It is not like an email")
    
# count the words of given string
# para = input("Enter your paragraph: ")
# words = para.split()
# print("No. of words:",len(words))

# count the number of vowels in given string as input

sentence = "hello how are you"
number_of_vowels = (
    sentence.lower().count("a") +
    sentence.lower().count("e") + 
    sentence.lower().count("i") + 
    sentence.lower().count("o") +
    sentence.lower().count("u")
)
# 1 + 2 + 0 + 3 + 1
# print(number_of_vowels)


# name = "aNIkeT    "

# # Hello Aniket
# # greeting_msg = "Hello"+ " " + name
# greeting_msg = f"Hello {name.strip().capitalize()}"

# check if the string is palindrome or not

# h = input("Enter your string:").strip().lower()

# if h == h[::-1]:
#     print("It is palindrome")
# else:
#     print("Not palindrome")

i = "Hello how are you   ".strip()
# "Hello how are you"
# ["Hello", "how", "are", "you"]
# "Hellohowareyou"
list_of_words = i.split(" ")
words_without_space = "".join(list_of_words)
# print("og str:", i)
# print("list:", list_of_words)
# print("words without space:", words_without_space)
print("count of alphabets:", len(words_without_space))