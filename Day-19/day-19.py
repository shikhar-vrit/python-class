from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass                    # no work here

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

# print(Square(4).area())     # 16
# print(Circle(2).area())
# r1 = Rectangle(8,6)
# print(r1.l)
# print(r1.w)
# print(r1.area())
# s = Shape()
# print(Rectangle(4, 2).area())



# shapes = [Square(4), Circle(2), Rectangle(6, 4)]

# for s in shapes:
#     print(s.area())



# from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def eat(self):                       # normal
        print(f"{self.name} is eatingg")

    @abstractmethod
    def sound(self):                     # must write
        pass

class Cow(Animal):
    def sound(self):
        print(f"{self.name} says Moo!")

class Dog(Animal):
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sound(self):
        print(f"{self.name} says woof.")

# c1 = Cow("Gauri")
# c1.eat()
# c1.sound()

# d1 = Dog("Tommy")
# d1.eat()
# d1.sound()


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

class Cash(Payment):
    def pay(self, amt):
        print(f"Paid Rs. {amt} with Khalti")

# Esewa().pay(500)
# Khalti().pay(200)
# Cash().pay(100)



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

# acc = BankAccount("Ram", 1000)
# print(acc.balance)

# acc.balance = -50000       # nobody stops this!
# print(acc.balance)         # -50000

# acc.balance = "hello"      # or this!
# print(acc.balance)



class Student:
    def __init__(self, name):
        self.name = name           # public

# s1 = Student("Ram")
# print(s1.name)        # Ram    (read from outside)

# s1.name = "Hari"      # change from outside
# print(s1.name)






class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance     # protected

acc = BankAccount("Ram", 1000)

# print(acc._balance)    # 1000   (works, but you shouldn't)
# acc._balance = 5
# print(acc._balance)






class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private

    def show(self):
        print(f"{self.owner}: Rs. {self.__balance}")
    # print({owner})

    def edit_bln(self, amt):
        self.__balance = amt
        print(f"balance edi to {self.__balance}")

acc = BankAccount("Ram", 1000)
# acc.show()          # Ram: Rs. 1000   (inside: OK)

# print(acc.owner)
# # print(acc.__balance)
# # acc.__balance = 2000
# acc.edit_bln(2000)
# acc.show()




class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):                 # getter
        return self.__balance

    def deposit(self, amount):             # setter
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Added Rs. {amount} and new balance Rs. {self.__balance}")
        else:
            print("Amount must be more than 0")

# acc = BankAccount("Ram", 1000)
# acc.deposit(500)            # Added Rs. 500
# acc.deposit(-200)           # Amount must be more than 0
# print(acc.get_balance())
# print(acc.__balance)






class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def check(self, pin):
        if pin == self.__pin:
            print("Welcome!")
        else:
            print("Wrong PIN")
    
    def change_pin(self, new_pin):
        self.__pin = new_pin
        print("pin updated succesfully")

acc = ATM(1234)
acc.check(1111)
acc.check(1234)

# acc.__pin = 1111
acc.change_pin(1111)
acc.check(1111)