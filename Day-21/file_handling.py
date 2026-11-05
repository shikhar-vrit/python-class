# f = open("notes.txt", "w")  

# f.write("Hello Nepal\n")
# f.write("Python is fun\n")

# f.close()


# with open("note.txt", "w") as f:
#     f.write("Hello\n")
#     f.write("Python\n")

# # the file is closed here, by itself

# print("Saved!")







# fruits = ["apple\n", "mango\n", "banana\n"]

# with open("fruits.txt", "w") as f:
#     f.writelines(fruits)
# print("Saved!")




# with open("fruit.txt", "w") as f:
#     f.writelines(["apple", "mango", "banana"])



# with open("notes.txt", "r") as f:
#     text = f.read()
# print(text)


# with open("notes.txt", "r") as f:
#     lines = f.readlines()
# print(lines)

# with open("notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())


# with open("notes.txt", "r") as f:
#     first = f.readline()
#     second = f.readline()
#     third = f.readline()

# print(first.strip())
# print(second.strip())
# print(third == "")



# with open("notes.txt", "w") as f:
#     f.write("New day\n")


# with open("notes.txt", "a") as f:
#     f.write("Momo is tasty\n")
#     f.write("Dal bhat power\n")


# with open("diary.txt", "r+") as f:
#     print(f.read())                    # 1. read first
#     f.write("Monday: learned files\n")


# with open("diary.txt", "r+") as f:
#     f.write("MON")


# with open("marks.txt", "r") as f:
#     print(f.read())


# try:
#     with open("marks.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File does not exist!")




import os

# os.remove("fruits.txt")          # fruits.txt is deleted


# if os.path.exists("fruit.txt"):
#     os.remove("fruit.txt")
#     print("Deleted!")
# else:
#     print("File not found")




# students = {"Ram": 80, "Sita": 92, "Hari": 75}

# # 1. Save: one student per line
# with open("marks.txt", "w") as f:
#     for name, marks in students.items():
#         f.write(f"{name},{marks}\n")

# # 2. Read back and find the total
# total = 0
# with open("marks.txt", "r") as f:
#     for line in f:
#         name, marks = line.strip().split(",")
#         print(name, "got", marks)
#         total = total + int(marks)

# print("Total:", total)




# with open("shop.txt", "w") as f:
#     f.write("rice\n")
#     f.write("dal\n")

# with open("shop.txt", "a") as f:
#     f.write("oil\n")

# with open("shop.txt", "w") as f:
#     f.write("salt\n")

# with open("shop.txt", "a") as f:
#     f.write("sugar\n")

# with open("shop.txt", "r") as f:
#     first = f.readline()
#     print(first)






class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

contacts = [Contact("Ram", "9841000001"),
            Contact("Sita", "9851000002")]


with open("contacts.txt", "w") as f:
    for c in contacts:
        f.write(str(c) + "\n")

# Add one more later
with open("contacts.txt", "a") as f:
    f.write(str(Contact("Hari", "9861000003")) + "\n")

# Read and show
with open("contacts.txt", "r") as f:
    for line in f:
        print(line.strip())