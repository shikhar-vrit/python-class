# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")


# for i in range(10):
#     print("Hello world")
#     print(i)



# fruits = ["apple", "mango", "banana"]

# for fruit in fruits:
#     print(fruit)

# print("Done!")  



# word = "Nepal abc"

# for letter in word:
#     print(letter)



# for i in range(10, 1, -1):
    # print(i)

# print(list(range(5)))


# total = 0

# for num in range(1, 11):
#     total += num          # same as total = total + num
#     print(f"Added {num}, total is {total}")

# print(f"Final total: {total}")



# prices = {"tea": 20, "coffee": 50, "momo": 150}

# for item in prices.items():                   
#     print(item)



# marks = [45, 80, 32, 67, 25]
# passed = 0
# failed = 0

# for m in marks:
#     if m >= 40:
#         print(f"{m}: Pass")
#         passed += 1
#     else:
#         print(f"{m}: Fail")
#         failed += 1

# print(f"{passed} students passed")
# print(f"{failed} students failed")


# count = 1

# while count <= 5:
#     print(count)
#     count += 1


# tasks = []

# task = input("Add a task (or 'quit'): ")

# while task != "quit":
#     tasks.append(task)
#     task = input("Add a task (or 'quit'): ")

# print("Your tasks:", tasks)



# n = 10

# while n > 0:
#     n -= 3
#     print(n)
    # n += 3

# print("Liftoff!")



# numbers = [4, 9, 10, 7, 15]

# for n in numbers:
#     if n >= 10:
#         print(f"Found a big one: {n}")
#         break
#     print(f"{n} is small")

# print("Loop over")




# for n in range(1, 8):
#     if n == 4:
#         continue       
#     print(n)


# list1 = [1, 5, 4, 6, 7, 8, 10 ,15, 32, 23, 45]

# for n in list1:
#     if n%2 == 0:
#         continue
#     print(n)

# names = ["ram", "sita", "gita", "hari", "shyam"]

# for name in names:
#     if name == "ram" or name == "sita":
#         continue
#     print(name)



# while True:
#     choice = input("Type 'hi' or 'exit': ").strip().lower()
    
#     if choice == "exit":
#         print("Bye!")
#         break
#     elif choice == "hi": #hi
#         print("Hello there!")
#     else:
#         print("I don't know that one")



# for row in range(1, 4):
#     for col in range(1, 6):
#         if col == 2 and row == 1:
#             continue
#         print(f"{row} x {col} = {row * col}")
#     print("---")


# for n in range(10):
#     if n % 2 != 0:
#         continue
#     if n > 7:
#         break
#     print(n)

# for i in range(1, 6, 2):
#     print("* " * i)

# print("Hello" * 5)

"""
*
***
*****
"""