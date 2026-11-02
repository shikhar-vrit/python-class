# print("Ram", "Sita", "Hari", sep=", ")

# for i in range(1, 6):
#     print(i, end=" ")


# num1 = float(input("enter number: "))
# print(type(num1))
# print(num1)

# print(int(1.9))

# num1 = int(input("enter number: "))
# print(type(num1))
# print(num1)


# num1 = 10
# # print(type(num1))
# # print(isinstance(num1, str))

# if isinstance(num1, int) and isinstance(num1, str):
#     print("num1 is integer or str")
# elif isinstance(num1, bool):
#     print("num1 is bool")
# elif isinstance(num1, str):
#     print("num1 is str")
# else:
#     print("num1 is not integer or bool or str")


# print(bool())

# print("a", "b", "c", sep="")
# print(int("7") + int(3.9))
# print(str(5) + str(5))
# print(float(4))
# print(bool(" "))
# print(len(set("hello")))
# print(int("10"))

# set1 = {"h", "e", "l", "o"}



#number
# print(abs(10))
# print(abs(-123))

# print(round(45.40))

# print(100 / 3)
# print(100 // 3)

# print(round(100/3, 3))

# print(2 ** 3)

# print(pow(2, 3))



# print(5//2, 13 % 5)

# print(divmod(13, 5))


# minutes = 135
#(135 // 60, 135 % 60)
# hours, mins = divmod(minutes, 60)
# print(f"{hours}hr, {mins}mins.")


# dict1 = {"tea": 20, "coffee": 50, "juice": 100}

# # print(sum(dict1.values()))



# marks = [67, 45, 92, 78]
# total = 0
# biggest = marks[0]
# smallest = marks[0]
# for m in marks:
#     total += m
#     if m > biggest:
#         biggest = m
#     if m < smallest:
#         smallest = m
# print(total, biggest, smallest) 


# print(sum(marks), max(marks), min(marks))



# def average(numbers=[1]):
#     return round(sum(numbers) / len(numbers), 2)

# number1 = [12, 35, 74, 12, 46, 74]

# print(average(number1))


# number2 = (12, 65, 2, 58, 56)
# print(average(number2))


# num3 = {1, 2, 2, 3, 4, 5, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6}
# print(average(num3))
# print(sum(num3))
# print(len(num3))



# print(abs(-7) + abs(3))
# print(round(9.87, 1))
# print(pow(3, 2))
# print(divmod(20, 6))

prices = [120, 80, 250, 50]
# print(f"Cheapest: {min(prices)}")
# print(f"Costliest: {max(prices)}")
# print(f"Total: {sum(prices)}")

# print(sorted(prices, reverse=True))

# word = "hello"
# print(sorted(word))

# dict1 = {"tea": 10, "coffee": 20, "juice": 30}

# print(sorted(dict1))

# num1 =  [2, 5, 23, 4, 7, 2, 9]

# print(list(reversed(num1)))




fruits = ["apple", "mango", "banana"]

count = 1
# for fruit in fruits:
#     print(f"{count}. {fruit}")
#     count += 1

# for num, fruit in enumerate(fruits, start=1):
#     print(f"{num}. {fruit}")



names = ["Ram", "Sita", "Hari"]
marks = [78, 92, 35]

# for name, mark in zip(names, marks):
#     print(f"{name} got {mark}")


# student_marks = dict(zip(names, marks))
# print(student_marks)
# print(student_marks.items())



# list1 = [True, False, True]
# print(all(list1))
# print(any(list1))


# marks = [78, 92, 45, 64]
# passed = []
# for m in marks:
#     passed.append(m >= 40)
# print(passed)
# print(all(passed))      # False: someone failed
# print(any(passed)) 



# words = ["momo", "tea", "chowmein", "dal"]

# print(sorted(words))
# print(sorted(words, key=len))
# print(max(words))
# print(min(words))

# print(max(words, key=len))
# print(min(words, key=len))


# def max():



names = ["Sita", "Ram", "Gita"]
ages = [21, 19, 23]

# print(len(names))
# print(sorted(names))
print(list(reversed(ages)))