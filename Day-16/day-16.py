# def run_twice(func):     # func is a function
#     func()                 # run it
#     func()                 # run it again

# def hello():
#     print("Hello!")

# def add():
#     print(100+150)

# run_twice(hello) 
# run_twice(add)


# def make_box():
#     def inner():
#         print("I am inner")
#     return inner         

# new_func = make_box()   
# new_func()


def add_line(func):           # 1. take a function
    def wrapper():              # 2. make a cover for it
        print("----------")
        # print("starting task")     #    extra work before
        func()                  #    run the real function
        print("----------")     #    extra work after
    return wrapper              # 3. give the cover back

# def say_hi():
#     print("Hi!")

# x = add_line(say_hi)       # put the cover on
# say_hi()
# x()

# @add_line
# def say_hi():
#     print("Hi!")

# say_hi()


# def my_decorator(func):
#     def wrapper():
#         # extra work BEFORE
#         print("before")
#         func()
#         # extra work AFTER
#     return wrapper          # no () here!

# @my_decorator
# def my_function():
#     print("my real work")

# my_function()


# def show(func):
#     def wrapper(*args):
#         print("Start")
#         answer = func(*args)     # pass the inputs on
#         print("End")
#         return answer            # give the answer back
#     return wrapper

# @show
# def add(a, b):
#     return a + b

# print(add(2, 3))




# def need_password(func):
#     def wrapper():
#         password = input("Password: ")
#         if password == "1234":
#             func()                  # correct: run it
#         else:
#             print("Wrong password!")
#     return wrapper

# @need_password
# def show_balance():
#     print("Balance: Rs. 5000")

# show_balance()


# def shout(func):
#     def wrapper():
#         print("HEY!")
#         func()
#         print("BYE!")
#     return wrapper

# @shout
# def eat():
#     print("Eating momo")

# @shout
# def sleep():
#     print("Sleeping")

# eat()
# sleep()







# def countdown(n):
#     if n == 0:              # Rule 1: base case
#         print("base case!")
#         return              # stop here
#     print(n)
#     countdown(n - 1)        # Rule 2: smaller step

# countdown(3)


# def sum_to(n):
#     if n == 1:                  # base case
#         return 1
#     return n + sum_to(n - 1)    # smaller step

# print(sum_to(4))     # 10   (4 + 3 + 2 + 1)
# print(sum_to(5))



# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))

# def sum_loop(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#         # total += i
#     return total

# # With recursion
# def sum_to(n):
#     if n == 1:
#         return 1
#     return n + sum_to(n - 1)

# print(sum_loop(4))    # 10
# print(sum_to(4))




# def stars(n):
#     if n == 0:
#         return
#     print("*" * n)
#     stars(n - 1)

# def double_sum(n):
#     if n == 0:
#         return 0
#     return 2 + double_sum(n - 1)

# stars(3)
# print(double_sum(4))




def three_numbers():
    yield 1
    yield 2
    yield 3

g = three_numbers()
# print(g)   
# print(next(g))     
# print(next(g))
# print(next(g)) 
# print(next(g)) 

# for n in g:
#     print(n)



def cook():
    print("Cooking plate 1...")
    yield "Plate 1"
    print("Cooking plate 2...")
    yield "Plate 2"
    print("Cooking plate 3...")
    yield "plate 3"

g = cook()      

# print(next(g))
# print(next(g))
# print(next(g))



def count_up(limit):
    n = 1
    while n <= limit:
        yield n          # give n, pause here
        n = n + 1        # continue from here next time

# for x in count_up(3):
#     print(x)


# print(list(count_up(5)))



def count_up(limit):
    n = 1
    while n <= limit:
        yield n
        n = n + 1

# g = count_up(5)
# print(list(g)) 
# print(list(g))



def squares_list(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result

# Generator: makes ONE at a time
def squares_gen(n):
    for i in range(1, n + 1):
        yield i * i

print(squares_list(4))         # [1, 4, 9, 16]
print(list(squares_gen(4)))