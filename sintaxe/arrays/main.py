# Arrays

from array import array

# Arrays are like lists, but they can only store one type of data
# The type of data is specified when creating the array
#  i = signed integer, l = signed long, f = floating point, d = double, etc

# Creating an array
numbers = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(numbers)

# Accessing array items by index
print(numbers[6])

# Adding items in the end of an array (only works with the same type of data)
numbers.append(11)
print(numbers)

# Adding items to an array
numbers.insert(5, 99)
print(numbers)

# Removing items from the end of an array
numbers.pop()
print(numbers)

# Removing an especific item from an array
numbers.remove(99)
print(numbers)

# Removing items from an array by index
del numbers[3]
print(numbers)

# Deleting an array
del numbers
