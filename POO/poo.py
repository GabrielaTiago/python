# Classes
# A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).

# self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class Car: # class name
    condition = 'new' # class variable

    def __init__(self,color, brand, model, top_speed) -> None:
        self.color = color # instance variable
        self.brand = brand
        self.model = model
        self.top_speed = top_speed

    # methods
    def turn_on(self):
        print('The car is on')

    def turn_off(self):
        print('The car is off')

    def info(self):
        print(f'Color: {self.color}')
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Top speed: {self.top_speed}')

    # class method
    @classmethod # decorator to indicate that the method is a class method
    def super_car(cls, brand, model): # cls is a reference to the class
       return cls("Black", brand, model, 450)

    @classmethod
    def daily_car(cls, brand, model):
        return cls("Gray", brand, model, 150)

    @staticmethod # decorator to indicate that the method is a static method
    def luxury_car(brand):
        if brand == 'Ferrari':
            return True
        else:
            return False

print(Car.condition) # new
print(Car.super_car('Ferrari', 'F40').color) # Black

print(Car.luxury_car('Ferrari')) # True
print(Car.luxury_car('Fiat')) # False

# creating an object
car = Car('Red', 'Ferrari', 'F40', 340)
print(car.color)
print(car.brand)
print(car.model)
print(car.top_speed)
car.turn_on()
car.turn_off()
car.info()
