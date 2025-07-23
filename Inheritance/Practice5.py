# Hierarchial Inheritance
# multiple child classes inherit from a single parent class.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def show_brand(self):
        print(f"Brand: {self.brand}")
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
    def show_details(self):
        self.show_brand()
        print(f"Car with {self.doors} doors")
class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc
    def show_details(self):
        self.show_brand()
        print(f"Bike with {self.cc}cc engine")
class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity
    def show_details(self):
        self.show_brand()
        print(f"Truck with {self.capacity} tons capacity")
c = Car("Toyota", 4)
b = Bike("Honda", 150)
t = Truck("Volvo", 10)
c.show_details()
print("------")
b.show_details()
print("------")
t.show_details()




