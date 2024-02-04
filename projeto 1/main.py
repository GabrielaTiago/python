from datetime import datetime
import random
import time

GIFT_CARDS = ['R$50,00','R$250,00','R$120,00']

def sorteia_cartao():
    # Espera 5 segundos
    time.sleep(5)
    return random.choice(GIFT_CARDS)

# Inicializando o programa
print("\nBem-vinddo(a) ao cadastro de usuários! \n\nPor favor, preencha os campos abaixo:\n\n\n")

# Entrada - Nome de usuário, idade, data de cadastro (automática)
username = input('Digite seu nome: ')
user_age = int(input('Digite sua idade: '))
birthdate = datetime.strptime(input('Digite sua data de nascimento (dd/mm/aaaa): '), '%d/%m/%Y')
register_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

print(f'\nOlá {username}, seu registro foi concluído com sucesso no dia {register_date}.')

print("\n\nEstamos sorteando um cartão de presente para você...\n\n")
user_gift_card = sorteia_cartao()

print(f'Parabéns! Você ganhou um cartão de presente no valor de {user_gift_card}!')

# Fim do programa