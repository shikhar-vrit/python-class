# print(7/2)
# print(7//2)
# print(7%2)
# print(3**2)


name = "  ram bahadur  "
# print(name.strip().title())


word = "Python "
# print(word[0], word[-1])      
# print(word[1:3])              
# print(len(word.strip()))

# num1 = int(float(input("Enter an number: ")))
# print(type(num1))
# print(num1)

# print(int("10.56"))


fruits = ["apple", "banana", "mango"]


fruits.append("kiwi")
# print(fruits)
fruits.insert(3, "grapes")
# print(fruits)

# fruits.remove("kiwi")
# print(fruits)

# fruit = fruits.pop(2)
# print(fruit)
# print(fruits[1:3:-1])

# for i in range(10,1,-2):
#     print(i)

tup1 = (10, 20)
names = ("ram", "hari", "sita", "gita")
# print(type(tup1))
# tup2 = ("10",)
# print(type(tup2))
# print(tup1[0])

# print(sum(tup1))
# print(max(names))

# num1, num2 = tup1
# print(num1)
# print(num2)


a = 5
b = 6
# temp = a
# a = b
# b = temp
# print(a, b)

a, b = b, a
# print(a, b)


a = {1, 2, 3, 3}
b = {2, 3, 4}

# print(a)
# print(len(a))
# print(a)
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)

# a |= b
# print(a)

a = set()



student = {"name": "Sita", "age": 20, "city":"bkt"}

# print(student["name"])
# print(student.get("grade"))

student["grade"] = "A"
# print(student.get("grade"))

# for key, value in student.items():
#     print(key, "->", value)



# marks = 92

# if marks >= 80:
#     print("pass")
# elif marks >= 40:
#     print("Distinction")
# else:
#     print("Fail")



# age = 10
# has_ticket = False
# if age >= 18 or has_ticket:
#     print("You can enter")


# menu = ["momo", "tea"]
# if "pizza" not in menu:
#     print("Sorry, no pizza")


# for i in range(1, 6):
#     print(i, end=" ")     
# print()


# count = 3
# while count > 0:
#     print(count)
#     count -= 1


# def print_num(a, b=0):
#     print(f"a: {a}, b: {b}")

# print_num(a=4)


# names = ["Ram", "Sita"]
# ages = [21, 19]
# for i, name in enumerate(names, start=-5): # (2, "Sita")
#     print(i, name)

# dict1 = {"name":"ram", 10:"ten", 10.50:"decimal", (12, 13):"tuple", "d1":{"name": "ram"}}
# print(dict1)

# def profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# profile(name="Gita", city="Pokhara", age=20)


# students = [("Ram", 78), ("Sita", 92), ("Hari", 35)]

# print(sorted(students, key=lambda s: s[1], reverse=True))

tup1 = ("Ram", 20, "KTM", "A")  # packing

name1, age, address, grade = tup1  # unpacking

print(f"name: {name1} \nage: {age} \naddress: {address} \ngrade: {grade}")