#  Dictinaries
#  A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# Creating a dictionary
person1 = {
    'name' : 'John',
    'lastname': 'Doe',
    'age': 30
}
person2 = dict(name='John', lastname='Doe', age=30)

print(person1)
print(person2)

# Accessing dictionary items
person2_idade = person2['age']
print(person2_idade)

# Accessing dictionary items using get method
person2_idade = person2.get('age')

# Getting all keys from a dictionary
keys = person1.keys()
print(keys)

# Getting all values from a dictionary
values = person1.values()
print(values)

# Getting all items from a dictionary
items = person1.items()
print(items)

# Looping through a dictionary
for item in items:
    print(item[0], item[1])

# Sorting by a dictionary key
from operator import itemgetter

products_list =[{'id':5, 'product': 'Notebook', 'price': 3000}, {'id':3, 'product': 'Smartphone', 'price': 1500}, {'id':1, 'product': 'Headphone', 'price': 100}, {'id':2, 'product': 'Mouse', 'price': 50}, {'id':4, 'product': 'Keyboard', 'price': 40}]

products_list.sort(key=itemgetter('product'))
print(products_list)

products_list.sort(key=itemgetter('price'), reverse=True)
print(products_list)

print('------------------')

# Dictionary comprehension
# Dictionary comprehension is an elegant and concise way to create dictionaries
# {key: expression for item in iterable}

from pprint import pprint
pprint({product['product']: [i*3 for i in range(5)] for product in products_list})
