import json

# Examples of json files and how to read their content

with open('sintaxe/json/users/usuarios1.json', encoding='utf-8') as file:
    data = json.load(file) # This will convert the json file into a dictionary
    print(data)
    print(data['nome'])
    print(data['admin'])
    # json_data = file.read()

with open('sintaxe/json/users/usuarios2.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(data['permissões'][2])

with open('sintaxe/json/users/usuarios3.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(data['usuários'][0]['permissões'][1])

with open('sintaxe/json/users/usuarios4.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(data['usuários'][0]['plano']['preco'])

with open('sintaxe/json/users/usuarios5.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(data[1]['telefone'])

# Creating a json file
user_data = '''{
    "nome": "João",
    "idade": 25,
    "email": "jao@email.com"
}'''

# Readind a string
data = json.loads(user_data)
print(data)

# Writing a json file
with open('sintaxe/json/users/user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

# Reading a json file
with open('sintaxe/json/users/user.json', encoding='utf-8') as file:
    data = json.load(file)
    print(data)
    print(data['nome'])
    print(data['idade'])
    print(data['email'])