from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        """Printeaza coordonatele punctului"""
        print(self.x, self.y)

    def move(self, x, y):
        """Se muta coordonatele punctului avand date noi valori"""
        self.x = x
        self.y = y

    def setToOrigin(self):
        """Se seteaza coordonatele x si y la 0, 0"""
        self.x = 0
        self.y = 0

    def dist(self, second_point):
        """Returneaza distanta dintre punct si un alt punc"""
        return sqrt((second_point.x - self.x) ** 2 + (second_point.y - self.y) ** 2)


point1 = Point(5, 7)
point2 = Point(11, 5)
point1.show()
print(point1.dist(point2))

point1.show()
point1.move(77, 29)

point1.show()

x = point1.dist(Point(22, 33))
print(x)
