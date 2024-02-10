# Tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in).
# Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

# Creating a tuple
sites = ('google.com', 'youtube.com', 'facebook.com', 'twitter.com')
values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(sites)
print(values)

print('------------------')

# Accessing tuple items by index
google = sites[0]
print(google)

print('------------------')

# Looping through a tuple
for site in sites:
    print(site)

print('------------------')

# Unpacking a tuple
a, b, c, d = sites
print(a)
print(b)
print(c)
print(d)

print('------------------')

# Unpacking a tuple with *
a, *b, c = values
print(a)
print(b)
print(c)

print('------------------')

# Tuples are immutable
# sites[0] = 'yahoo.com' # This will raise an error

# Joining tuples
new_tuple = sites + values
print(new_tuple)

# Deleting a tuple
del new_tuple

# Getting the length of a tuple
print(len(sites))

# Adding items to a tuple
# sites.append('yahoo.com') # This will raise an error
