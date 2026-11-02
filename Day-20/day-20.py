class Car:
    def move(self):
        print("Car drives on the road")

class Boat:
    def move(self):
        print("Boat sails on the water")

class Plane:
    def move(self):
        print("Plane flies in the sky")

class House:
    def rooms(self):
        print("House has 5 rooms")

    # def move(self):
    #     print("Plane flies in the skyyyyy")

c1 = Car()
b1 = Boat()
p1 = Plane()

# c1.move()
# b1.move()
# p1.move()

x= 6
x = 10


vehicles = [Car(), Boat(), Plane()]

# for v in vehicles:
#     v.move()


def start_trip(vehicle):
    print("Trip started!")
    vehicle.move()

# start_trip(Car())
# start_trip(Boat())
# start_trip(Plane())
# start_trip(House())




class Nepali:
    def greet(self):
        print("Namaste")

class English:
    def greet(self):
        print("Hello")

class Japanese:
    def greet(self):
        print("Konnichiwa")

class Robot:
    def greet(self):
        print("Beep beep")

people = [Nepali(), English(), Japanese(), Robot()]

# for p in people:
#     p.greet()









class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} flies high")

class Sparrow(Bird):
    def fly(self):
        print(f"{self.name} flies low")                          # uses parent fly()

class Penguin(Bird):
    def fly(self):                 # override
        print(f"{self.name} cannot fly, it swims")

class Kiwi(Bird):
    def fly(self):                 # override
        print(f"{self.name} cannot fly, it runs")

# for b in [Sparrow("Chiri"), Penguin("Pingu"), Kiwi("Kiki"), Bird("happy")]:
#     b.fly()




class Employee:
    def __init__(self, name="Ram"):
        self.name = name

    def salary(self):
        return 20000

class Manager(Employee):
    def salary(self):              # override
        return 80000

class Intern(Employee):
    def salary(self):              # override
        return 10000

class mid_employee(Employee):
    pass

staff = [Employee(), Manager(), Intern(), mid_employee("Hari")]

# total = 0
# for s in staff:
#     print(s.name, s.salary())
#     total = total + s.salary()

# print("Total:", total)







from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Esewa(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with eSewa")

class Khalti(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with Khalti")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} with card")

def checkout(method, amount):
    method.pay(amount)

# checkout(Esewa(), 500)
# checkout(Khalti(), 1000)
# checkout(Card(), 1500)







class Shape:
    def area(self):
        return 0

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

class Dot(Shape):
    pass

# for s in [Square(3), Rectangle(4, 5), Dot()]:
#     print(s.area())



class Calculator:
    def add(self, a, b, c=0):         
        return a + b + c

    def total(self, *args):            
        return sum(args)

calc = Calculator()

# print(calc.add(2, 3))                # 5
# print(calc.add(2, 3, 4))             # 9

# print(calc.total(1, 2))              # 3
# print(calc.total(1, 2, 3, 4, 5, 6, 7, 12, 53, 67, 23))



class Greet:
    def hello(self, name="Friend", times=1):
        for i in range(times):
            print(f"Hello {name}")

# g = Greet()
# g.hello()
# g.hello("Ram")
# g.hello("Sita", 2)