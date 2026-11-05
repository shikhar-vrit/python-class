# import greetings 
from greetings import say_hello, SHOP_NAME



# print(greetings.SHOP_NAME)
# greetings.say_hello("Ram")
# greetings.say_bye("Ram")

# print(SHOP_NAME)
# say_hello("Ram")



import greetings as g
# g.say_hello("Ram")
# g.say_bye("Ram")
# print(g.SHOP_NAME)




from shapes import Square, Circle

s = Square(4)
c = Circle(2)

# print(s.area())      # 16
# print(c.area())




from logger import announce

@announce
def add(a, b):
    return a + b

@announce
def sub(a, b):
    return a - b

# print(add(3, 4))
# print(sub(4, 3))






from cart import bill

# print(bill(2, 1))


import greetings
# greetings.say_hello("Sita")


# from greetings import say_hello
# from greetings import say_hi

# def main():
#     name = input("Your name: ")
#     say_hello(name)

# if __name__ == "__main__":
#     main()







class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks          # goes through the setter

    @property
    def marks(self):                # getter
        return self._marks

    @marks.setter
    def marks(self, value):         # setter
        if value < 0 or value > 100:
            raise ValueError("Marks must be 0 to 100")
        self._marks = value

s = Student("Ram", 80)
print(s.marks)      # 80   (getter, no brackets)
s.marks = 100
print(s.marks)