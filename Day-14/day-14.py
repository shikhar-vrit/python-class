# def my_decorator(func):
#     def wrapper():
#         print("----- start -----")
#         func()
#         print("----- end -----")
#     return wrapper

# def say_hello():
#     print("Hello!")

# def say_hi():
#     print("Hi!")


# say_hello = my_decorator(say_hello)
# say_hello()
# say_hi = my_decorator(say_hi)
# say_hi()

# @my_decorator
# def say_bye():
#     print("Bye!")

# say_bye()



# def my_decorator(func):
#     print("1. decorating", func.__name__)

#     def wrapper():
#         print("3. before")
#         func()
#         print("5. after")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("4. Hello!")

# # say_hello()
# print("2. now we call it")
# say_hello()


# def add(a, b):
#     print(a + b)

# add()



# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Calling", func.__name__)
#         result = func(*args, **kwargs)
#         print("Done")
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a + b

# total = add(3, 4)
# print(total)




logged_in = True
is_authorized = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("Please log in first!")
            return
        elif not is_authorized:
            print("You dont have permission.")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
def see_balance():
    print("Balance: Rs. 5000")

# see_balance()    
# logged_in = True
# see_balance()



# def stars(func):
#     def wrapper():
#         print("*****")
#         func()
#         print("*****")
#     return wrapper

# def dashes(func):
#     def wrapper():
#         print("-----")
#         func()
#         print("-----")
#     return wrapper

# @stars
# @dashes
# def hello():
#     print("Hello!")

# hello()



def double_it(func):
    def wrapper(n):
        return func(n) * 2
    return wrapper

def say(func):
    def wrapper():
        print("Before")
        func()
    return wrapper

@double_it
def add_ten(n):
    return n + 10

@say
def hi():
    print("Hi")

# print(add_ten(10))
# hi()
# print(add_ten(0))
# add_ten()

def countdown_loop(n):
    while n > 0:
        print(n)
        n -= 1
    print("Go!")

# countdown_loop(5)


def countdown(n):
    if n == 100:         # Base case     
        print("Go!")
        return
    print(n)
    countdown(n - 1)   # Recursive case

# countdown(1)


def factorial(n):
    if n == 1:                      # base case
        return 1
    return n * factorial(n - 1)     # smaller step

# print(factorial(100))






def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

# print(total(5))              

# Reverse a word
def reverse(word):
    if word == "":
        return ""
    return reverse(word[1:]) + word[0]

# print(reverse("abcd"))       # omom

# Add all items in a list
def list_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + list_sum(nums[1:])

# print(list_sum([4, 5, 6]))   # 15


import sys
# print(sys.getrecursionlimit())



def power(base, n):
    if n == 0:
        return 1
    return base * power(base, n - 1)

def count_down(n):
    if n == 0:
        return "Done"
    print(n)
    return count_down(n - 1)

def digits(n):
    if n < 10:
        return 1
    return 1 + digits(n // 10)

# print(power(2, 3))
# print(power(5, 0))
# print(count_down(3))
# print(digits(4567))
# print(digits(7))






def get_numbers():
    return [1, 2, 3]

# print(get_numbers())


def gen_numbers():
    yield 1
    yield 2
    yield 3

# print(gen_numbers())

# for n in gen_numbers():
#     print(n)


def gen_numbers():
    yield 1
    yield 2
    yield 3

g = gen_numbers()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def steps():
    print("Start")
    yield "A"
    print("Middle")
    yield "B"
    print("End")

g = steps()

# print(next(g))
# print(next(g))
# print(next(g))


def count_up(limit):
    n = 1
    while n <= limit:
        yield n
        n += 1

# for num in count_up(5):
#     print(num, end=" ")     
# print()

def evens(limit):
    for n in range(limit + 1):
        if n % 2 == 0:
            yield n

# print(list(evens(10)))



def token_numbers():
    n = 1
    while True:
        yield n
        n += 1

# token_numbers()
tokens = token_numbers()
# print(next(tokens))
# print(next(tokens))


def count_up(limit):
    # return "Hello"
# var1 = count_up() # var1 = "Hello"
# print(var1)
# print(var1)

    for n in range(1, limit + 1):
        return n


# nums = count_up(3)
# print(list(nums))
# print(list(nums))


# squares_list = [n * n for n in range(5)]
# print(squares_list)         # [0, 1, 4, 9, 16]



# Round brackets: a generator, one by one
# squares_gen = (n * n for n in range(5))
# print(squares_gen)          # <generator object <genexpr> at 0x...>
# print(list(squares_gen))    # [0, 1, 4, 9, 16]

# # Inside a function call, one pair of brackets is enough
# print(sum(n * n for n in range(5)))


import sys

big_list = list(range(1000000))
big_gen = (n for n in range(1000000))

# print(sys.getsizeof(big_list))   # 8000056  (about 8 MB)
# print(sys.getsizeof(big_gen))    # 200      (tiny!)

# print(sum(big_list))             # 499999500000
# print(sum(big_gen))