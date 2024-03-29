# Loop and collections

# For
# range(start, stop, jump)
for word in range(1, 6):
    print('Loading...')

print('------------------')

# Number list with range 1 to 5
for item in range(1, 6):
    print(item)

print('------------------')

# Number list with range 20 to 40 and jump 2
for item in range(20, 41, 2):
    print(item)

print('------------------')

# While loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1

print('------------------')

# While loop with break
counter = 76
while True:
    print(counter)
    counter += 1
    if counter == 80:
        break

print('------------------')

# Collections
# Names list with 4 names
names = ['João', 'Maria', 'José', 'Ana']
for name in names:
    print(name)

print('------------------')

# Ages list with 3 ages
ages = [33, 89, 27]
for age in ages:
    print(age)

print('------------------')

# Mixed list with 3 names and 3 ages
mixed = ['João', 33, 'Maria', 89, 'José', 27]
for item in mixed:
    print(item)

print('------------------')

# Aceessing list items by index
print(mixed[0])
print(mixed[1])

print('------------------')


celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(f'{celular} - {versao}')

print('------------------')

values = [1,2,3,4,5,6,7,8,9,10]
years = [1990,1991,1992,1993,1994,1995,1996,1997,1998,1999]

# Add a new item to the end of the list
values.append(100);

# Add a new item to the list in the position x
values.insert(3, 99)

# Remove the last item from the end of the list
values.pop()

# Remove the first item from the list
values.pop(0)

# Remove a range of items from the list
del values[0:3]

# Remove the first item with the value 5
values.remove(5)

# Remove all items from the list
values.clear()

# Join two lists
values.extend(years)

# Create a new list with the join of two lists
new_list = values + years



# SORT LISTS
arr = [3, 5, 1, 9, 7, 2, 8, 4, 6]
print(arr)

# Sort the list in ascending order
arr.sort()

# Sort the list in descending order
# arr.sort(reverse=True)

# Reverse the list
# arr.reverse()
print(arr)

print('------------------')

# Loop in two lists
from itertools import zip_longest

products = ['Celular', 'Notebook', 'Carregador', 'Fone', 'Mouse', 'Teclado', 'Monitor', 'Cadeira', 'Mesa', 'Geladeira']
prices = [1000, 3000, 100, 50, 30, 40, 300, 500]

for product, price in zip_longest(products, prices):
    print(f'O preço do {product} é R$ {price}')

print('------------------')

# Enumerate
# Enumerate returns a tuple with the index and the item
#  enumerate(iterable, start=0)
#   iterable - a sequence, an iterator, or objects that supports iteration
#   start - the index value from which the counter is to be started, by default it is 0

names = ['João', 'Maria', 'José', 'Ana', 'Carlos', 'Mariana', 'Pedro', 'Paula']

for index, name in enumerate(names, start=1):
    print(f'{index} - {name}')
    if index == 3:
       print('Temos 3 nomes na lista')

print('------------------')

# Map
# Map applies a function to all the items in an input_list
#  map(function_to_apply, list_of_inputs)

def square(number):
    return number * number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(square, numbers))
print(squared)

# Filter
# Filter creates a list of elements for which a function returns true
#  filter(function, list)

def is_even(number):
    return number % 2 == 0

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_even = list(filter(is_even, numbers))
print(list_even)

# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Sets are unordered, so the items will appear in a random order.
# Does not allow duplicate items

# Creating a set
s_numbers = [1, 2, 3, 4, 5, 6, 7, 2, 8, 9, 10]
print(s_numbers)

fruits = {'apple', 'banana', 'cherry', 'banana', 'orange', 'kiwi', 'melon', 'mango', 'grape', 'apple'} # Duplicate items will be removed from the set
print(fruits)

set_numbers = set(s_numbers)
print(set_numbers)

set_fruits = set(list(fruits))
print(set_fruits)

# Adding items to a set
set_numbers.add(11)
print(set_numbers)

# Removing an item from a set
set_numbers.remove(11)
print(set_numbers)

# Removing an item from a set using discard
set_numbers.discard(10)
print(set_numbers)

# Removing the first item from a set
set_numbers.pop()
print(set_numbers)

# Clearing a set
set_numbers.clear()
print(set_numbers)

# Deleting a set
del set_numbers

# Joining sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

# Joining two sets
s1 = set1.union(set2)
print(s1)

# Joining two sets using update
set1.update(set2)
print(set1)

numbers1 = [2,5,6,2,8]
mumbers2 = [2,3,4,5,6,7,5,8,9,10]

n1 = set(numbers1)
n2 = set(mumbers2)

# Symmetric difference (items that are not in both sets)
print(n1.symmetric_difference(n2))

# Intersection (common items)
print(n1.intersection(n2))

# Union (all items)
print(n1.union(n2))

print('------------------')

# list comprehension
# List comprehension is an elegant way to define and create lists based on existing lists.
# [expression for item in iterable if condition == True]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)