# Dictionary

# collection of multiple different data types stored as an key:value pairs

# keys -> unique
# values -> can be duplicate

# dictionary is mutable
# dictionary is unordered

# student_data = ["Aniket", 10, "test@test.com"]

student_data = {
    "fname" : "Aniket",
    "lname" : "Raj",
    3.14 : "PI",
    10 : "TEN",
    (1,2) : "Data",
    "age" : 10,
    "emails" : ["test@test.com","test1@test.com"],
    "address" : {
        "street" : "xyz",
        "city" : "G Noida",
        "state" : "UP",
        "pincode" : 201310
    }
}

# print(student_data.get("address").get("pincode"))
# print(student_data["address"]["pincode"])
# print(student_data["emails"][1])
# print(student_data)
# print(type(student_data))
# print(student_data["fname"])


# get(key,default = None) -> Any | None => READ

# print(student_data.get("mobile",9876543210))


# empty_dict = {}
# empty_dict = dict([0,1,2])
empty_dict = list({"n":"b","m":"c"})
# print(empty_dict)

# list => dict ❌
# dict => list -> [keys] ✅

# CREATE

product = {
    "title": "Tshirt",
    "price" : 199
}
product["category"] = "clothing"
product["price"] = product["price"] + product["price"] * 0.3

# del product["title"]
# product.pop("title")
print(product.popitem()) # -> (key,value) =>removes last key value pair
# product.clear()
# print(list(product.keys())) # => dict_keys -> list
print(list(product.values())) # => dict_values -> list
product.setdefault("sizes",["S","M","L"])
print(product["sizes"])



"""
A college wants to maintain basic information about its students. Write a Python program to create a dictionary where the student's roll number is the key and the student's name is the value. 
1. Create an empty dictionary.
2. Take the roll number and name of multiple students from the user and store them in the dictionary. 
3. Display the complete student dictionary.
4. For the following input, write the expected output: 
Roll Number: 101, Name: Rahul 
Roll Number: 102, Name: Aman

"""


students = {}
number_of_students = int(input("Enter number of students: "))
for st in range(number_of_students):
    roll_number = input("Enter roll number: ")
    st_name = input("Enter name: ")
    students[roll_number] = st_name

print(students)

# any one you can use either commented code or uncommented code to display the student dictionary

# keys = list(students.keys())
# values = list(students.values())
# for i in keys:
#     print(f"Roll Number: {i}, Name: {values[keys.index(i)]}" )

for key, value in students.items():
    print(f"Roll Number: {key}, Name: {value}" )
