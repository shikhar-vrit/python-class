class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r