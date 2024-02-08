# Functions
# Pattern: lowercase, snake case

# Defining a function
# def name_of_function(*parameters, **default_parameter = 'x'): *Optional | if a parameter is not passed, the default value is used, usually the last parameter
#     # Code block

# 1
def salute(nome: str):
    message = "Hello, " + nome + "! Wellcome!"
    return message

# Calling 1
user_name = input("Enter your name:")
result = salute(user_name)
print(result)

# Return a value
def return_calculated_value(price: float, quantity: int = 1):
    result = price * quantity
    return result

# Print a value, does not return
def print_calculated_value(price: float, quantity: int = 1):
    result = price * quantity
    print(result)

# Multiple returns (tuple)
def multiple_returns(price: float, quantity: int = 1):
    result = price * quantity
    return price, quantity, result

# Multiple returns (dictionary)
def multiple_returns(price: float, quantity: int = 1):
    result = price * quantity
    return {'price': price, 'quantity': quantity, 'result': result}

# Multiple returns (list)
def multiple_returns(price: float, quantity: int = 1):
    result = price * quantity
    return [price, quantity, result]

# Multiple returns (set)
def multiple_returns(price: float, quantity: int = 1):
    result = price * quantity
    return {price, quantity, result}


def rectangle_area(length, width):
    return length * width

#  POSICIONAL PARAMETERS (args)
# The order of the parameters is important
rectangle_area(10, 20)

# NAMED PARAMETERS
# The order of the parameters is not important
rectangle_area(width=20, length=10)

# Keyword-only arguments are specified after an asterisk in the parameters list
def rectangle_area_2(*, length, width):
    return length * width

# rectangle_area_2(10, 20) <- ERROR -> CORRECT: rectangle_area_2(length=10, width=20)

# Dynamic number of parameters

# *args: tuple
def sum(*args, n):
    result = 0
    for number in args:
        result += number
    return result + n

sum(1, 2, 3, 4, 5, n=10) # 25

# **kwargs: dictionary (key-value)
def create_person(**kwargs):
    print(kwargs)

create_person(name='John', age=30, height=1.80, weight=80)


# Decorators
# A decorator is a function that takes another function as an argument and adds some kind of functionality to it.
# This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

# Decorator example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# @my_decorator
def say_hello():
    print("Hello!")

# @my_decorator is the same as:
# result = my_decorator(say_hello)
# result()

# the @ is just a short way of saying:
# say_hello = my_decorator(say_hello)
# say_hello()