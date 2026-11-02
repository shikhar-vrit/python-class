# tup1 = ("tea", "coffee", "milk", "momo")

# item1, item2, item3, item4 = tup1

# print(item1)
# print(item2)
# print(item3)
# # print(item4)



# def welcome():
#     print("=====================")
#     print("Welcome to Momo House")
#     print("=====================")

# welcome()
# welcome()
# welcome()
# welcome()


# greet()
# def greet():
#     print("Namaste!")

# greet()

# def show_stars():
#     for i in range(1, 4):
#         print("*" * i)

# for n in range(2):
#     show_stars()

# def line():
#     print("~~~~~~~~~~~~~~")

# def happy():
#     print("Happy Dashain!")

# line()
# happy()
# line()




# def greet(name, age, class1):
#     print(f"Hello, {name}, age: {age}, class: {class1}")

# greet("ram", 25, "nursery")
# greet("sita")


# def add(a, b):
#     print(a + b)

# add(2, 3)

# add(2)

# def cart(bread=2, milk=1):
#     print(f"bread: {bread}, milk: {milk}")

# cart(1, 4)

# def introduce(name, age):
#     print(f"I am {name}. I am {age} years old.")

# introduce(name="Gita", age=21)
# introduce(age=21, name="Gita")
# introduce("sita", 22)
# introduce(22, "sita")



# def show_menu(menu):
#     print("--- MENU ---")
#     for item, price in menu.items():
#         print(f"{item}: Rs. {price}")
# # ("coffee", 50) (20, "tea")
# tea_shop = {"tea": 20, "coffee": 50}
# momo_shop = {"veg momo": 120, "chicken momo": 150}

# show_menu(tea_shop)
# show_menu(momo_shop)


def box(word, symbol="#"):
    line = symbol * (len(word) + 4)
    print(line)
    print(f"{symbol} {word} {symbol}")
    print(line)

# box("Nepal")
# box("*", "hi")
# box(symbol="+", word="Python")


# def add(a, b):
#     return a + b
#     # print(a+b)

# result = add(2, 3)
# print(result)

# result = add(10, 100) + add(100, 200)
# print(result)



def check_result(mark=30):
    if mark >= 40:
        return "Pass"
    return "Fail"
    print("This never prints")
    print("hi")

# print(check_result(75))     # Pass
# print(check_result(30))     # Fail

# status = check_result(60)
# print(f"Ram: {status}")


def is_even(n):
    return n % 2 == 0

# print(is_even(4))    # True
# print(is_even(7))    # False

# numbers = [3, 8, 10, 5, 6]
# count = 0
# for n in numbers:
#     if is_even(n):
#         count += 1

# print(f"{count} even numbers")

def lowest_highest(marks):
    return min(marks), max(marks)

marks = [67, 45, 92, 78]

result = lowest_highest(marks)
# print(result) 

# low, high = result
# print(f"high: {high}")
# print(f"low: {low}")


# def double(n):
#     return n * 2

# def shout(word):
#     print(word.upper() + "!")

# x = double(5)
# print(x + 1)
# print(double(double(3)))

# y = shout("hello")
# print(y)

# bill = 400

# def make_bill():
#     global bill
#     bill = 500
#     print(f"Inside: {bill}")

# make_bill()
# print("outside:", bill)



def subtotal(price, qty):
    return price * qty

def add_vat(amount):
    # def hello():
    #     print("hello")
    # hello()
    return amount + amount * 0.13


def bill_total(price, qty):
    before = subtotal(price, qty)
    # print("before:", before)
    return add_vat(before)

# print(subtotal(150, 2))     # 300
# print(add_vat(300))         # 339.0
# print(bill_total(150, 2))


def add(a, b):
    """It sum 2 numbers and print the answer."""
    print(a + b)

add(1, 2)


# help(add)


