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

print('-------------------')

# creating an object using class method
car2 = Car.super_car('Lamborghini', 'Aventador')
print(car2.color)
print(car2.brand)
print(car2.model)
print(car2.top_speed)
car2.info()

print('-------------------')

# Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class ElectricCar(Car):
    def __init__(self, color, brand, model, top_speed, battery) -> None:
        super().__init__(color, brand, model, top_speed) # calling the parent class constructor
        self.battery = battery

    def info(self):
        super().info() # calling the parent method
        print(f'Battery: {self.battery}')

    def turn_on(self):
        print('The electric car is on')

    def turn_off(self):
        print('The electric car is off')

    def charge(self):
        print('The car is charging')

electric_car = ElectricCar('Blue', 'Tesla', 'Model S', 250, '100kWh')
electric_car.info()
electric_car.turn_on()

print('-------------------')

# Multilevel inheritance

# When a class is derived from another derived class, it is called multilevel inheritance.
# It is similar to single inheritance, but the difference occurs when a class is derived from another derived class.
# The class is derived from another derived class.
# Multilevel inheritance is bad for maintainability and readability, so it should be avoided. (heigth acoplament, height complexity, height risk of bugs, etc.)

class SportsCar(Car):
    def __init__(self, color, brand, model, top_speed, sport_package) -> None:
        super().__init__(color, brand, model, top_speed)
        self.sport_package = sport_package

    def info(self):
        super().info()
        print(f'Sport package: {self.sport_package}')

class SuperCar(SportsCar):
    def __init__(self, color, brand, model, top_speed, sport_package, super_package) -> None:
        super().__init__(color, brand, model, top_speed, sport_package)
        self.super_package = super_package

    def info(self):
        super().info()
        print(f'Super package: {self.super_package}')

class HyperCar(SuperCar):
    def __init__(self, color, brand, model, top_speed, sport_package, super_package, hyper_package) -> None:
        super().__init__(color, brand, model, top_speed, sport_package, super_package)
        self.hyper_package = hyper_package

    def info(self):
        super().info()
        print(f'Hyper package: {self.hyper_package}')

hyper_car = HyperCar('Yellow', 'Bugatti', 'Chiron', 420, 'Sport', 'Super', 'Hyper')
hyper_car.info()

print('-------------------')

# Multiple inheritance

# In multiple inheritance, the **features** of all the base classes are inherited into the derived class.
# The class derived from multiple classes is called a derived class.

class A:
    def method(self):
        print('Method A')

class B:
    def method(self):
        print('Method B')

class C(A, B):
    pass

c = C()
c.method() # Method A (the method of the first class is called)
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A


# Dunder methods

# Dunder methods are special methods with double underscores at the beginning and end of their names.
# They are also called magic methods.
# They are used to create functionality that can't be represented as a normal method.
# They are used to define the behavior of objects.
# They are called automatically by Python interpreter.

class Book:
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

book = Book('Clean Code', 'Robert C. Martin', 464)
print(book) # Clean Code by Robert C. Martin
print(len(book)) # 464
del book # A book object has been deleted

# Abstract classes

# Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
# Abstract classes are used to define a blueprint for other classes.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    # pass # TypeError: Can't instantiate abstract class Dog with abstract methods move

    # implementing the abstract method of the parent class
    def move(self):
        print('The dog is walking')

class Bird(Animal):
    def move(self):
        print('The bird is flying')

# animal = Animal() # TypeError: Can't instantiate abstract class Animal with abstract methods move
dog = Dog()
dog.move() # The dog is walking
bird = Bird()
bird.move() # The bird is flying

