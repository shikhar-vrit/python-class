# print(int("10.56"))

# var1 = int(input("Entrer an number: "))
# print(var1)

# print("2" + "2")

# print(5/0)


# var1 = 20
# print(var2)

# list1 = [1, 4, 5, 7, 1, 8]

# print(list1[7])

# try:
#     age = int(input("Enter your age: "))
#     print("Next year you will be", age + 1)
# except ValueError:
#     print("Please type a positive integer number!")

# print("Program continues...")


# try:
#     a = int(input("First number: "))
#     b = int(input("Second number: "))
#     print("Answer:", a / b)
# except ValueError:
#     print("Please type numbers only.")
# except ZeroDivisionError:
#     print("You can't divide by zero.")



# print(int("12ssd"))

# try:
#     num = int("12abc")
# except ValueError as e:
#     print("Error:", e)

# try:
#     print(10 / 0)
#     # num = int("12abc")
# except (ValueError, ZeroDivisionError) as e:
#     print("Problem:", e)






# def check_age(text):
#     try:
#         age = int(text)
#     except ValueError:
#         print("Not a number!")
#     else:
#         print("Your age is", age)
#     finally:
#         print("--- check done ---")

# check_age("10")




# nums = [10, 20, 30]

# try:
#     print(nums[1])
#     print(nums[3])
#     print("A")
# except IndexError:
#     print("B")
# else:
#     print("C")
# finally:
#     print("D")



# print("7"+3)


# try:
#     print(int("7") + 3)
# except ValueError:
#     print("E")
# else:
#     print("F")


# while True:
#     try:
#         age = int(input("Enter your age: "))
#         break
#     except ValueError:
#         print("That's not a number. Try again.")

# print("Thanks! Your age is", age)



def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Numbers only, please!")

# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Can't divide by zero"

# x = get_number("First number: ")
# y = get_number("Second number: ")

# print(safe_divide(b=y, a=x))



# age = -5

# if age < 0:
#     raise ValueError("Age can't be negative")

# print("Age saved")


# def set_age(age):
#     if age < 0:
#         raise ValueError("Age can't be negative")
#     print("Age saved:", age)

# # set_age(-20)

# try:
#     set_age(5)
# except ValueError as e:
#     print("Error:", e)


try:
    age = int(input("Enter your age: "))

    if age < 18 or age < 0:
        raise ValueError("Age must positive and 18 or above!")

    print("Access granted!")

except ValueError as e:
    print("Error:", e)

print("Program continues...")