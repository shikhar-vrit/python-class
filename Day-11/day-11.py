# def tea(name, sugar):
#     print(f"{name} wants tea with {sugar} sugar")

# tea(sugar=2, name="Ram")

# def add(a, b):
#     print(a + b)

# add(2,items 3, 6, 7)


# def add(*numbers):
#     total = 0
#     print(numbers)
#     for n in numbers:
#         total += n
#         # total = 7 + 6
#         # total = 13
#     return total

# print(add(3, 4, 6, 4, 6, 10, 23, 40))


# def show(*items):
#     print(items)
#     print(type(items))
#     print(len(items))

# show("bread", "coffee", "sugar", "honey")
# show()

# def report(*marks):
#     print(f"Count:   {len(marks)}")
#     print(f"Total:   {sum(marks)}")
#     print(f"Highest: {max(marks)}")
#     print(f"Lowest:  {min(marks)}")
#     print(f"Sorted:  {sorted(marks)}")
#     print(f"listed: {list(marks)}")
#     listed = list(marks)
#     listed.append(96)
#     print(f"new listed: {listed}")
#     # marks.append(67)
#     # print(marks)

# report(67, 45, 92, 78)



# def show(item1, *items):
#     print(item1)
#     print(type(item1))
#     print(items)
#     print(type(items))
#     print(len(items))

# show("bread", "coffee", "sugar", "honey")



# def greet(greeting, *names):
#     for name in names:
#         print(f"{greeting}, {name}!")

# greet("Namaste", "Ram", "Sita", "Hari")


# def greet(greeting, *names):
#     print("greeting =", greeting)
#     print("names    =", names)

# greet("Namaste", "Ram", "Sita", "Hari")

# print("a")
# print("a", "b", "c")
# print("a", "b", "c", "d", "e", sep="-")


# def total(*prices, discount=0):
#     amount = sum(prices)
#     return amount - amount * discount / 100

# print(total(100, 200, 300, discount=10))


# def count(*things):
#     return len(things)

# def first(*things):
#     return things[0]

# def join_all(sep, *words):
#     return sep.join(words)

# print(count(1, 2, 3))
# print(count())
# print(first("tea", "coffee"))
# print(join_all("##", "a", "b", "c"))
# print(first())


# def profile(**info):
#     print(info)
#     print(type(info))


# profile(name="ram", age = 25, adress="KTM")

# empty_set = set()
# empty_dict = {}


# def profile(**info):
    
#     for key, value in info.items():
#         print(f"{key}: {value}")
#     print("----")

# profile(name="Sita", age=22, city="Kathmandu", grade="A")
# profile(name="Hari", hobby="football")


# def order_tea(**options):
#     sugar = options.get("sugar", 1)
#     milk = options.get("milk", "yes")
#     milks = options.get("milks", "no")
#     print(f"Tea: sugar={sugar}, milk={milk}, milks={milks}")
#     print(f"Options sent: {len(options)}")

# order_tea(milk="no")


# def student(name, **marks):
#     #marks = {"math": 88, "science": 76, "english": 91}
#     print(marks)
#     print(f"Student: {name}")
#     print(marks.items())
#     for subject, mark in marks.items():
#         print(f"  {subject}: {mark}")
#     print(f"  Total: {sum(marks.values())}")

# student("Gita", math=88, science=76, english=91)


# def names(**names):
#     #{"ram": "name"}
#     # print(names.keys())
#     # print(names.values())
#     # print(names.items())
#     for a, b in names.items():
#         print(f"{a}: {b}")

# names(first_name="ram")



# def info(**details):
#     return details

# def count(**details):
#     return len(details)

# print(info(a=1, b=2))
# print(count(x=10, y=20, z=30, a=20))
# print(info())

# def momo(plate, **extras):
#     print(f"{plate} momo")
#     for name, amount in extras.items():
#         print(f"  - {name} x{amount}")

# # momo("Buff", achar=2, soup=1)
# # momo("Veg", "achar")
# momo("veg")

# def demo(a, *args, b=0, **kwargs):
#     print("a      =", a)
#     print("args   =", args)
#     print("b      =", b)
#     print("kwargs =", kwargs)


# demo(1, 4, 5, 7, 89, 90, 2, 3, x=10, y=20)

# demo(1, 4, 5, 7, 89, 90, 2, 3)

# demo(1, x=10, y=20)



# def add(a, b, c):
#     return a + b + c

# nums = [10, 20, 30]

# # Long way
# print(add(nums[0], nums[1], nums[2]))   # 60

# # Short way
# print(add(*nums)) 



# print("hello \t world")


# fruits = ["apple", "mango", "banana"]

# print(fruits)              
# print(*fruits)             
# print(*fruits, sep="\n")
# print(*fruits, sep="\t")

# print(*"hello world")


# def profile(name, age, city):
#     print(f"{name}, {age}, from {city}")

# ram = {"name": "Ram", "age": 21, "city": "Pokhara"}

# profile(**ram)

# def total(*prices):
#     return sum(prices)

# cart = [120, 80, 250]
# more = (50, 30)

# print(total(*cart))
# print(total(120, 80, 250))   
# print(total(*more))        
# print(total(*cart, *more))    
# print(total(*cart, 100))      
# print(total(cart))



marks = [92, 78, 67, 45, 30]

first, *rest = marks
print(first)     
print(rest)

top, *middle, last = marks
print(top) 
print(middle)
print(last)