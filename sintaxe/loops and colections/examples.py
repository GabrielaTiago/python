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

# Desafios 🥇

# 1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela
items = ['Celular', 'Notebook', 'Carregador']
print(items[0], items[1], items[2])
print(list(items))

# 2 Usando apenas uma linha de código, crie uma lista de 10 a 131
numbres = list(range(10, 132))
print(numbres)

# 3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
new_list = list(items) + list(numbres)
print(new_list)

# 4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos que você mais usa durante o dia,
# mas agora dentro de cada item você vai colocar uma informação extra, coloque o valor em reais desse objeto também e imprima ele na tela
values = [1000, 3000, 100]
items_and_values = [[items[0],values[0]], [items[1], values[1]], [items[2], values[2]]]
print(items_and_values)

# 5 Itere sobre a lista abaixo exibindo o número do indice + nome da fruta. Porém quando o indice for 3, exiba "Nº do indice + nome da fruta EM PROMOÇÃO"
PROMO_TEXT = ''
fruits = ['Maçã', 'Laranja' ,'Morango', 'Pera', 'Abacaxi']

for index, fruit in enumerate(fruits):
    if index == 3:
        PROMO_TEXT = 'EM PROMOÇÃO'
    print(f'{index} - {fruit} {PROMO_TEXT}')
    PROMO_TEXT = ''

# 6 Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

DESIRED_SALARY = 2500

jobs = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]

def min_salary(job):
    return job[1] > DESIRED_SALARY

filtered_jobs = list(filter(min_salary, jobs))
print(filtered_jobs)