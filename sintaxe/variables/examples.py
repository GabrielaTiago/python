# Exemplos de variáveis
print('Vamos codar!')
print('Vamos \'codar!\'')
print('''Vamos
\'codar\'''')

print('------------------')

# Desafio 1

## Crie os seguinte strings dinâmicos
from unidecode import unidecode

nome = 'Carol'

hobby = 'ouvir Música'

str_ex = 'Olá sou a Carol e gosto de ouvir musica'
made_str = f'Olá sou a {nome} e gosto de {unidecode(hobby.lower())}'
str_comp = f'String propsta: \'{str_ex}\'\nString montada: {made_str}\n'

if(str_ex == made_str):
    print(f'{str_comp}São iguais! Parabéns!')
else:
    print(f'{str_comp}São diferentes! Tente novamente!')

print('------------------')

# Desafio 2

## Monte a seguintes palavras, usando as sílabas como base

b = 'ba'

parte2 = 'nica'

a = 'a'

r = 'ri'

parte1 = 'eletrô'

t = 'te'

# Resultado

str_ex = 'bateria eletrônica'
made_str = f'{b}{t}{r}{a} {parte1}{parte2}'
# also works:
# made_str = b + t + r + a + ' ' + parte1 + parte2
str_comp = f'String propsta: \'{str_ex}\'\nString montada: {made_str}\n'

if(str_ex == made_str):
    print(f'{str_comp}São iguais! Parabéns!')
else:
    print(f'{str_comp}São diferentes! Tente novamente!')

print('------------------')

# DESAFIO 3🥇

# Através da criação de string dinâmicos e os métodos de um string que acabou de aprender, use como base as variáveis a seguir para criar as seguintes frases

a = 'é'

b = 'MELHOR'

c = 'QUE '

d = ' feito'

e = 'perfeito'

print(f'{a.capitalize()} {b.lower()} {d.lstrip()} {c.lower().rstrip()} {e}!')

print('------------------')

# Desafio 4 => Encontre o índice de 'o' dentro da variável "bbiblioteca"
biblioteca = 'Biblioteca'
print('O index de \'o\' em biblioteca é ', biblioteca.index("o"))

# Desafio 5 => Usando a frase 'Desenvolvimento De Aplicações', imprima apenas "De Aplicações"
desafio = 'Desenvolvimento De Aplicações'
words = desafio.split(' ')
print(words[1] + ' ' + words[2])

indice_d = desafio.rindex('D')
indice_s = desafio.rindex('s')
print(desafio[indice_d:indice_s+1])

print('------------------')

frase1 = 'Desafio manipulação de strings'

frase2 = 'jhonatan,rafael,carol,camilla'
# ​Desafio 6 => Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
palavras1 =  frase1.split(' ')
print(palavras1)

# Desafio 7 => Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
palavras2 = frase2.split(',')
print(palavras2)

# Desafio 8 => Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
print(','.join(palavras1))

# Desafio 9 => Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.
print(' & '.join(palavras2))

print('------------------')

# DESAFIO 10 => Calcule quantos dias falta, ate ao seu aniversario
from datetime import datetime

today = datetime.now()
print('today: ', today.strftime('%d/%m/%Y %H:%M:%S'))

birthday = datetime(2024,4,14)
print('birthday: ', birthday.strftime('%d/%m/%Y %H:%M:%S'))

diff = birthday - today
print('Quantos dias até meu aniversário', diff.days)

print('------------------')


import random

# DESAFIO 11 => Simule a opção de jogar uma moeda e resultar em CARA ou COROA jogue as opções dentro de uma variável e depois crie um programa que imprimir a seleção na tela
board = ['CARA', 'COROA']
print("cara ou coroa: ", random.choice(board))

# DESAFIO 12 => Crie uma lista de 5 nomes, realize um sorteio de acordo com essa lista e exiba o sorteado na tela
names = ['Jhonatan', 'Rafael', 'Carol', 'Camilla',  'Gabriela']
print('Selected name: ',random.choice(names))

# DESAFIO 13 => Imprima na tela um valor aleatório entre 10 e 100
random_number = random.randint(10, 100)
print('Ramdom number: ',random_number)

print('------------------')

