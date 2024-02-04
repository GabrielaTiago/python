# Desafio 🥇
# Defina as seguintes variáveis: possui_passaporte, passagem_comprada, menor_de_idade, inicialmente todas como False.
# Crie as seguintes condições em # e imprima o resultado na tela.

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

# Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade
print(possui_passaporte and passagem_comprada and (not menor_de_idade))

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(possui_passaporte or (passagem_comprada and (not menor_de_idade)))

# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((not possui_passaporte) or (possui_passaporte and (not menor_de_idade)))

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print((not possui_passaporte) or ((not passagem_comprada) and menor_de_idade))

print('\n------------------\n')

# Desafio 🥇
# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras:
'''
Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
Acima de 50cm Favor consultar na recepção
'''
# Declare uma variável que represente o tamanho atual do cabelo
# Imprima na tela a mensagem apropriada

TAMANHO_CABELO_CURTO = 20
TAMANHO_CABELO_MEDIO = 30
TAMANHO_CABELO_GRANDE = 50

tamanho_cabelo_cliente = 25
# tamanho_cabelo_cliente = int(input('Qual o tamanho do seu cabelo? '))

if tamanho_cabelo_cliente <= TAMANHO_CABELO_CURTO:
    print('O valor do corte é R$50,00')
elif TAMANHO_CABELO_CURTO < tamanho_cabelo_cliente <= TAMANHO_CABELO_MEDIO:
    print('O valor do corte é R$70,00')
elif TAMANHO_CABELO_MEDIO < tamanho_cabelo_cliente <= TAMANHO_CABELO_GRANDE:
    print('O valor do corte é R$100,00')
else:
    print('Favor consultar na recepção')

print('\n------------------\n')

# DESAFIO 🥇
# Ese expressão condicional(operador ternário) para criar a seguinte condição
# se velocidade estiver acima de 100 exibir, você foi multado, caso contrário exiba siga em frente

velocidade = 101
print('Você foi multado') if velocidade > 100 else print('Siga em frente')