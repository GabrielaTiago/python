# Chute o número
#
# Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10. O usuário deverá chutar um número até que acerter o valor aleatório gerado no inicio do programa.
# O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

import random

# Entrada - Recebe um número inteiro (Nº do chute)
number = int(input('Chute um número de 1 a 10: '))

# Validação - O número deve estar no intervalo de 1 a 10
while number < 1 or number > 10:
    print('O número deve estar entre 1 e 10.')
    number = int(input('Chute novamente um número de 1 a 10: '))

# Processamento - Gera um número aleatório de 1 a 10
random_number = random.randint(1, 10)

while number != random_number:
    # Saída - Informa se o chute foi acima ou abaixo do valor aleatório gerado comparando o número com o número aleatório gerado
    if number < random_number:
        print(f'O número {number} é menor que o número aleatório.')
    elif number > random_number:
        print(f'O número {number} é maior que o número aleatório.')
    # Nova entrada
    number = int(input('Digite um novo número: '))

# Saída - Sucesso
print(f'Parabéns! Você acertou o número {random_number}.')