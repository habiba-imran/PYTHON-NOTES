# Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"{self.x}i + {self.y}j"
v1 = Vector(1, 2)
v2 = Vector(4, 5)
print(v1)
print(v2)
print(v1 + v2)
print(type(v1 + v2))
# with vector added in add function, it returns vector object

