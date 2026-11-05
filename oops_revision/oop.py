class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Some sound")
    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # parent sets name
        self.breed = breed        # child adds breed
    def sound(self):              # override
        print("Woof!")

# d = Dog("Tommy", "Husky")
# d.eat()       
# d.sound()
# print(d.name)
# print(d.breed)





from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def show(self):                
        print("Area:", self.area())

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):                
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
        
    def area(self):
        return self.l * self.w

# Square(4).show()    # Area: 16
# Rectangle(6, 4).show()
# Shape()






class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks       

    def get_marks(self):          
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be 0 to 100")

s = Student("Ram", 80)
# # print(s.name)
# # print(s.__marks)
# s.set_marks(90)        
# print(s.get_marks())    
# # print(s.__marks)




class Staff:
    def pay(self):
        return 0
    
    # def pay(self):
    #     return 10

class Teacher(Staff):
    def pay(self):
        return 40000

class Driver(Staff):
    def pay(self):
        return 25000

total = 0
# for person in [Teacher(), Driver(), Staff()]:
#     total += person.pay()       # same call, different answer
# print(total)



class Esewa:
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        print(f"Paid {self.amount} with esewa.")

class Khalti:
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        print(f"Paid {self.amount} with khalti.")

e1 = Esewa(500)
k1 = Khalti(1000)
# e1.pay()
# k1.pay()




class Calculator:
    def add(self, a, b=0, c=0):     # way 1: default values
        return a + b + c

    def total(self, a, *nums):         # way 2: *args
        return sum(nums)

c = Calculator()
# print(c.add(5))
# print(c.add(5, 10)) 
# print(c.add(5, 12, 15))
# # print(c.add(5, 13, 14, 15))
# print(c.total(5, 5, 5, 5))




class Duck:
    def quack(self):
        print("Quack quack!")

class Person:
    def quack(self):
        print("I am saying quack!")

class Toy:
    def quack(self):
        print("Squeak quack!")

def make_it_quack(thing):
    thing.quack()                 # no type check

# for t in [Duck(), Person(), Toy()]:
#     make_it_quack(t)




class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f"{self.owner}: Rs {self.__balance}"

class Savings(Account):
    def deposit(self, amount):
        super().deposit(amount + 10)    # bonus

for acc in [Account("Ram", 100), Savings("Sita")]:
    acc.deposit(50)
    print(acc)

a = Account("Hari", 150)
a.__balance = 0
print(a.get_balance())
