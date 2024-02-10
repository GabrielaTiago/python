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
