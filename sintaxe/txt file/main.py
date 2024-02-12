"""
HOW TO CREATE AND MODIFY FILES:
    'w' - write
    'r' - read
    'a' - append
    'r+' - read and write
    'w+' - write and read
    'a+' - append and read
"""

import os

PATH = 'sintaxe/txt file/test.txt'

names = ['João', 'Maria', 'José', 'Ana', 'Carlos']
numbers = [1, 2, 3, 4, 5]
# aways convert the data to string before writing in a file

# 'w' - use to write in a file (if the file doesn't exist, it will be created)
with open(PATH, 'w', encoding='utf-8') as file:
    file.write('Hello World!')

# # 'a' - use to append in a file (if the file doesn't exist, it will be created)
with open(PATH, 'a', newline='', encoding='utf-8') as file:
    file.write('Nomes dos alunos:\n' + os.linesep)
    for number, name in zip(numbers, names):
        file.write(f'{number} - {name}' + os.linesep)

# 'r' - use to read a file (if the file doesn't exist, it will raise an error)
with open(PATH, 'r', encoding='utf-8') as file:
    for row in file:
        print(row, end='')
    print(file.read()) # read the entire file

# 'r+' - use to read and write in a file (if the file doesn't exist, it will raise an error)
with open(PATH, 'r+', newline='' ,encoding='utf-8') as file:
    for row in file:
        print(row, end='')
    file.write('6 - Fernanda' + os.linesep)

