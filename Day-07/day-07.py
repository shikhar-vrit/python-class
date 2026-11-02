# num = float(input("Enter a number: "))

# if num > 100:
#     print("number is more than 100")

# print("Success!") 


# age = int(input("Enter you age: "))

# if age >= 18:
#     print("You can vote!")
# else:
#     print("You can not vote yet!")
# print("Thank you!")



# marks = float(input("Enter you marks: "))

# if marks >= 80:
#     print("Your grade is A")
# elif marks >= 60:
#     print("Your grade is B")
# elif marks >= 40:
#     print("Your grade is C")
# else:
#     print("Failed!")




# temp = 18

# if temp > 30:
#     print("Hot day")
# elif temp > 20:
#     print("Nice day")
# else:
#     print("Cold day")

# print("Done")

# if temp = 18:
#     print("Exactly 18")


age = 16
has_idcard = False

# if age >= 18 or has_idcard:
#     print("You can vote")
# else: 
#     print("you can not vote")


# if not has_idcard:
#     print("you can vote")
# else:
#     print("you can not vote")


# cart = ["eggs", "bread", "milk"]

# # print("eggs" in cart)

# if "eggs" in cart:
#     print("we have eggs")
# else: 
#     print("We don't have eggs")



# prices = {"tea": 20, "coffee": 50}
# prices["juice"] = 100
# item = input("Order: ")
# if item in prices:
#     print(f"Price: Rs. {prices[item]}")
# else:
#     print("Sorry, not on the menu")

# answer = input("Do you like Python? ")

# if answer.strip().title() == "Yes":
#     print("Great! Me too")
# else:
#     print("You will soon!")



# name = input("Your name: ")

# if name:
#     print(f"Hello, {name}")
# else:
    # print("You didn't type anything")


# cart = ["bread"]
# if not cart:
#     print("Your cart is empty")
# else:
#     print("there is some items in you cart")


# username = input("Username: ")
# password = input("Password: ")
# role = input("Enter your role (admin or user): ")

# if username == "admin":
#     if password == "1234":
#         if role == "admin":
#             print("welcome admin")
#         else:
#             print("welcome user")
#     else:
#         print("Wrong password")
# else:
#     print("User not found")




# day = input("Day: ")

# # with if / elif
# if day == "sat":
#     print("Holiday")
# elif day == "fri":
#     print("Half day")
# else:
#     print("School day")

# # with match-case (Day 03)
# match day:
#     case "sat":
#         print("Holiday")
#     case "fri":
#         print("Half day")
#     case _:
#         print("School day")




age = 18
city = "Pokhara"
friends = ["Ram", "Sita"]

# if age >= 28 and city == "Pokhara":
#     print("A")
# elif age >= 18 or city == "Pokharaa":
#     print("B")
# else:
#     print("C")

# if "Ram" not in friends:
#     print("ram is new")

if friends:
    print("You have friends")