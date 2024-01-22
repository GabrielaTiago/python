# Loop and collections

# For
# range(start, stop, jump)
for word in range(1, 6):
    print('Loading...')

# Number list with range 1 to 5
for item in range(1, 6):
    print(item)

# Number list with range 20 to 40 and jump 2
for item in range(20, 41, 2):
    print(item)

# While loop
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# While loop with break
counter = 76
while True:
    print(counter)
    counter += 1
    if counter == 80:
        break

# Collections
# Names list with 4 names
names = ['João', 'Maria', 'José', 'Ana']
for name in names:
    print(name)

# Ages list with 3 ages
ages = [33, 89, 27]
for age in ages:
    print(age)