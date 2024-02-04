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

# DESAFIOS 🥇
# Use a operação necessária(break ou continue) para que a seguinte condição aconteça:

# 1. Ao cegar ao estilo "Rap" o mesmo não deve ser impresso na tela
rhythms = ['Hip-Hop','Rock','Rap','Pop']
print('1: ')
for rhythm in rhythms:
    if rhythm == 'Rap':
        continue
    print(rhythm)

# 2. Ao chegar ao estilo "Rock" a execução deve interrompida
rhythms = ['Hip-Hop','Rock','Rap','Pop']
print('2: ')
for rhythm in rhythms:
    if rhythm == 'Rock':
        break
    print(rhythm)