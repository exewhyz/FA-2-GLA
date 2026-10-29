# Read a file
# file = open("hello.txt","r")
# data = file.read(5)
# file.close()
# print(data)

# Write a file
# f = open("new.txt","w")
# d = f.write("I am new file")
# f.close()
# print(d)

# f = open("new.txt","w")
# d = f.write("I am writing again")
# f.close()
# print(d)


# Append into a file
# f1 = open("new.txt", "a")
# f1.write("\nI am using append mode.")
# f1.close()

# with open("new.txt", "w") as f:
#     f.write("hello")


# file.read(size=-1) -> str
# -1 means everything
# file.write("content") -> int

"""
modes
1. r -> read
2. w -> write
3. a -> append
4. b -> binary
5. x -> create
6. t -> text
7. rb -> read binary
8. wb -> write binary
9. ab -> append binary
10. r+ -> read and write
11. +w -> Read and write
12. +a -> read and append
"""


# f = open("hello.txt", "r")
# data1 = f.read(2)
# data2 = f.read(2)
# data3 = f.read(2)
# print(data1)
# print(data2)
# print(data3)
# f.close()


# st_name = input("Enter your Name: ")
# st_marks = int(input("Enter your total marks: "))

# with open("student_data.txt","a") as fl:
#     fl.write(f"{st_name} : {st_marks}\n")


# no_of_students = int(input("Enter no. of students to add: "))

# for st in range(no_of_students):
#     st_name = input("Enter your Name: ")
#     st_marks = int(input("Enter your total marks: "))
    
#     with open("student_data.txt","a") as fl:
#         fl.write(f"{st_name} : {st_marks}\n")
        
# with open("student_data.txt","r") as file:
    # for line in file:
    #     print(line)
    # print(file.readline())
    # print(file.readline())
    # print(file.readlines())
    
# read() -> str
# readline() -> str
# readlines() -> [str...]

# with open("testing.txt", "w") as f:
#     f.write("car\n")
#     f.write("boat")

# data = ["bike","cycle"]
# with open("testing.txt", "w") as f:
#     # f.writelines(data)
#     for d in data:
#         f.write(d+"\n")

# f = open("new.txt")
# with open("new.txt") as f:
#     print(f.read())
#     print("inside with",f.closed)

# print("outside with",f.closed)

# seek(), tell() and truncate()

# seek(int)
# tell() -> int

with open("new.txt", "r+") as f:
    print("before seek",f.tell())
    f.seek(2)
    print("after seek",f.tell())
    print(f.truncate())
    print("after truncate",f.tell())