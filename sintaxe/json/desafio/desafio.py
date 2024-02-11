# Desafio 🥇
# Imprimir o e-mail do usuário com id 2
# imprimir a city do usuário com id 1
# Imprimir o total do pedido do usuário com id 2

import json

USER_1 = 1
USER_2 = 2

with open('sintaxe/json/desafio/desafio.json', encoding='utf-8') as file:
    data = json.load(file)
    user_list = data['user']

    for user in user_list:
        if user['id'] == USER_1:
            print(user['email'])
            print(user['address']['city'])
        elif user['id'] == USER_2:
            print(user['orders'][0]['total'])
