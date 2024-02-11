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


# Crie um arquivo json com a segunte estrutura:
'''
{
    "name": "João da Silva",
    "age": 30,
    "city": "Rio de Janeiro",
    "isStudent": false,
    "pga": 7.5
}
'''

user_data = '''{
    "name": "João da Silva",
    "age": 30,
    "city": "Rio de Janeiro",
    "isStudent": false,
    "pga": 7.5
}'''

data = json.loads(user_data)

with open('sintaxe/json/desafio/user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

with open('sintaxe/json/desafio/user.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(data['name'])
    print(data['age'])
    print(data['city'])
    print(data['isStudent'])
    print(data['pga'])
