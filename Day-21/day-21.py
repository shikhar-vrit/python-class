class Duck:
    def quack(self):
        print("Quack quack!")

class Person:
    def quack(self):
        print("I am saying quack!")

class Toy:
    def quack(self):
        print("Squeak quack!")

class Stone:
    def roll(self):
        print("Stone rolls")

def make_it_quack(thing):
    try:
        thing.quack()
    except AttributeError:
        print("This thing cannot quack.")

# make_it_quack(Duck())          # Quack quack!
# make_it_quack(Person())        # I am saying quack!
# make_it_quack(Toy())
# make_it_quack(Stone())         





class Phone:
    def charge(self):
        print("Phone is charging")

class Laptop:
    def charge(self):
        print("Laptop is charging")

class Book:
    def read(self):
        print("Reading the book")

def plug_in(device):
    try:
        device.charge()
    except AttributeError:
        print("Cannot charge this!")

# for d in [Phone(), Laptop(), Book()]:
#     plug_in(d)








class Student:
    def __init__(self, name, marks):
        # print("__init__ is running...")
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"{self.name} - {self.marks} marks"

s1 = Student("Ram", 80)

# print(s1.name)
# print(s1.marks)

# print(s1)


# text = str(s1)
# print(text)



class Basket:
    def __init__(self, fruits):
        self.fruits = fruits             # a list

    def __len__(self):
        return len(self.fruits)

b = Basket(["apple", "mango", "banana"])

# print(len(b))



class Wallet:
    def __init__(self, money):
        print("__init__ running")
        self.money = money

    def __add__(self, other):
        return Wallet(self.money + other.money)

    def __str__(self):
        return f"Rs. {self.money}"

# w1 = Wallet(500)
# w2 = Wallet(300)

# w3 = w1 + w2  # Wallet(800)

# print(w1)





class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

ram = Student("Ram", 80)
sita = Student("Sita", 92)
hari = Student("Hari", 80)

# print(ram == sita)
# print(ram == hari)
# print(ram < hari)
# print(hari < sita)





class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Muna Madan", 120)
b2 = Book("Python Basics", 300)

# print(b1)
# print(len(b2))
# print(b1 + b2)