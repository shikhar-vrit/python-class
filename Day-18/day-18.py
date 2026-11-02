# print(len({1, 2, 3, 1}))




class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):      # replaces the first add
        return a + b + c

calc = Calculator()
# print(calc.add(1, 2, 3))  

# print(calc.add(1, 2))





x = 50 
x = 100 




class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

# print(calc.add(2, 3))       # 5    (c = 0)
# print(calc.add(2, 3, 4))




class Student:
    def __init__(self, name):
        self.name = name

    def greet(self, time=""):
        if time == "":
            print(f"Hi, I am {self.name}")
        else:
            print(f"Good {time}, I am {self.name}")

# s1 = Student("Ram")
# s1.greet()               
# s1.greet("morning")






class Calculator:
    def add(self, *numbers):
        return sum(numbers)

calc = Calculator()

# print(calc.add(5))
# print(calc.add(5, 10, 15, 20, 25))



class MomoShop:
    def order(self, item, plates=1):
        price = 150 * plates
        print(f"{plates} plate {item}: Rs. {price}")

shop = MomoShop()

# shop.order() 
# shop.order("buff momo")
# shop.order("buff momo", 2)




class Greeter:
    def hello(self, name="friend", times=1):
        for i in range(times):
            print(f"Hello, {name}!")

g = Greeter()

# g.hello()
# g.hello("Sita")
# g.hello("Hari", 2)





class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!") 

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")             

c1 = Cat("Tommy")
d2 = Dog("goldy")
# d2.eat() 
# d2.bark()  
# c1.eat()
# c1.meow()         


a1 = Animal("Lion")
# a1.eat()
# a1.bark()



d1 = Dog("Tommy")
a1 = Animal("Lion")

# print(isinstance(d1, Dog))
# print(isinstance(d1, Animal))
# print(isinstance(a1, Dog))





class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4

    def start(self):
        print(f"{self.brand} started")

class Bike(Vehicle):
    def ring(self):
        print("Tring tring!")

b1 = Bike("Honda")
# b1.start()
# b1.ring()
# b1.wheels = 2
# print(b1.wheels)





class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):        
        print("Woof!")

class Cat(Animal):
    def sound(self):             
        print("Meow!")

class Fish(Animal):
    pass                          

# Dog("Tommy").sound()
# Cat("kitty").sound()
# Fish("nemo").sound()


animals = [Dog("Tommy"), Cat("Kitty"), Fish("Nemo")]

# for a in animals:
#     print(a.name, end=": ")
#     a.sound()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school       # only school is saved

s1 = Student("Ram", 20, "Skill Shikshya")
# print(s1.school)  
# print(s1.age)
# print(s1.name)






class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        super().introduce()                # parent's part
        print(f"I teach {self.subject}")   # child's part

# t1 = Teacher("Ram", "Python")
# t1.introduce()






class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.wheels = 4

    def info(self):
        print(f"{self.brand} has {self.wheels} wheels")

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.wheels = 2

car = Vehicle("Toyota")
bike = Bike("Honda")

# car.info()
# bike.info()
# print(bike.brand)



class Father:
    def house(self):
        print("I have a house")

class Son(Father):
    def bike(self):
        print("I have a bike")

s = Son()
# f = Father()
# s.house()    
# s.bike()
# f.house()


class Grandfather:
    def land(self):
        print("Land from grandfather")

class Father(Grandfather):
    def house(self):
        print("House from father")

class Son(Father):
    def bike(self):
        print("My own bike")

# s = Son()
# s.land()
# s.house()
# s.bike()
# f = Father()
# f.house()
# f.land()


class Person:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

s = Student("Ram")
t = Teacher("Sita")

# s.walk()      # Ram is walking
# t.walk()      # Sita is walking
# s.study()     # Ram is studying
# # s.teach()
# t.teach()
# t.study()



class Father:
    def height(self):
        print("Tall like father")

class Mother:
    def eyes(self):
        print("Brown eyes like mother")

class Child(Father, Mother):
    pass

# c = Child()
# c.height()   
# c.eyes()



class Person:
    def breathe(self):
        print("Breathing")

class Student(Person):
    def study(self):
        print("Studying")

class Worker(Person):
    def work(self):
        print("Working")

class Intern(Student, Worker):
    pass

# i = Intern()
# i.breathe()   # Breathing
# i.study()     # Studying
# i.work()      # Working





class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Added Rs. {amount}")

    def show(self):
        print(f"{self.owner}: Rs. {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=5):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate / 100
        self.deposit(interest)

acc = SavingsAccount("Ram", 1000)
acc.deposit(500)       # Added Rs. 500
acc.show()
acc.add_interest()     # Added Rs. 75.0
acc.show()