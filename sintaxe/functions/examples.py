# Desafios🥇

# 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
def creates_full_name(name: str, lastname: str):
    message = "Hello, " + name + " " + lastname + "! Wellcome!"
    return message

user_name = input("Enter your name: ")
user_lastname = input("Enter your lastname: ")
result = creates_full_name(user_name, user_lastname)
print(result + "\n")

# 2 - Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.
def calculates_values(price: float, quantity: int = 1):
    result = price * quantity
    return result

price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))
result = calculates_values(price, quantity)
print(result + "\n")

# 3 - Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato. A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
#     Porém ela deve seguir as seguintes regras:
#        1 - O primeiro argumento deve ser posicional
#        2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
def creates_custom_object(color: str, *, height: float, format: str):
    print(f"Color: {color}\nHeight: {height}\nFormat: {format}")

creates_custom_object("Red", height=10, format="Square")

# Parametros dinâmicos (args, kwargs)
def calculate(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for karg in kwargs.values():
        print(karg)

calculate('John', 1, 2, 3, 4, 5, age=30, height=1.80, weight=80)