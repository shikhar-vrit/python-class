# print(type("abc"))

class Student:
    pass              # empty for now

# s1 = Student()        # make an object
# s2 = Student()        # make another object

# print(type(s1))

# s1 = Student()
# s1.name = "Ram"       # s1's name
# s1.age = 20


# s2 = Student()
# s2.name = "Hari"       # s1's name
# s2.age = 22

# s3 = Student()
# s3.name = "sita"

# print(s1.name)
# print(s2.name)
# print(s3.age)



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student(20, "ram")
# # s2 = Student("Sita", 21)

# print(s1.name, s1.age)     # Ram 20
# print(s2.name, s2.age)




class Student:
    def __init__(self, name, age):
        self.name = name     # from the input
        self.age = age       # from the input
        self.marks = 0       # same start for everyone

s1 = Student("Ram", 20)
s2 = Student("Sita", 25)
# print(s1.name, s1.age, s1.marks)


# s1.marks = 50
# print(s1.name, s1.age, s1.marks)

# s1.age = 21
# print(s1.name, s1.age, s1.marks)
# print(s2.name, s2.age, s2.marks)

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        self.battery = 100

m1 = Mobile("Samsung", 30000)
m2 = Mobile("Redmi", 18000)

m1.battery = 40

# print(m1.brand, m1.battery)
# print(m2.brand, m2.battery)
# print(m1.price + m2.price)




class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name}")

s1 = Student("Ram", 20)
s2 = Student("Sita", 21)

# s1.greet()
s2.name = "Gita"
# s2.greet()








class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Added Rs. {amount}, Your new Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money!")
        else:
            self.balance = self.balance - amount
            print(f"Took Rs. {amount}, Your remaining balance: {self.balance}")

# acc = BankAccount("Ram")
# acc.deposit(1000)      # Added Rs. 1000
# acc.withdraw(300)      # Took Rs. 300
# acc.deposit(4000)
# acc.withdraw(5000)     # Not enough money!
# print(acc.balance)










class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def is_square(self):
        return self.length == self.width

r1 = Rectangle(5, 3)
r2 = Rectangle(4, 4)

# print(r1.area())         # 15
# print(r2.area())         # 16
# print(r1.is_square())    # False
# print(r2.is_square())




class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"{item} added.")

    def count(self):
        return len(self.items)
    
    def remove(self, item):
        self.items.remove(item)
        print(f"{item} has been removed.")

c1 = Cart("Ram")
c2 = Cart("Sita")

# c1.add("momo")
# c1.add("tea")
# c2.add("chowmein")
# c2.add("tea")
# print(c1.count())
# print(c2.count())
# c1.remove("tea")
# print(c1.count())
# print(c2.count())







class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)
        print(f"{mark} added to {self.name} new mark list {self.marks}")

    def average(self):
        return sum(self.marks) / len(self.marks)

    def report(self):
        avg = self.average()
        total = sum(self.marks)
        if avg >= 40:
            print(f"{self.name}: {avg} Pass total: {total}")
        else:
            print(f"{self.name}: {avg} Fail total: {total}")

s1 = Student("Ram")
s1.add_mark(80)
s1.add_mark(70)
s1.add_mark(0)
s1.add_mark(0)
s1.report()
