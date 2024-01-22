# Problema 2 - Contar de 1 a N

# Entrada - O programa deve receber um número inteiro N.
numero = int(input('Digite um número: '))

# Processamento - O programa deve imprimir todos os números de 1 até N.
for i in range(1, numero+1):
    # Saída - O programa deve imprimir um número por linha.
    print(i)


## Incremento - Contar de M a N

# Entrada - O programa deve receber dois números inteiros M e N.
numero_inicial = int(input('Digite o número inicial: '))
numero_final = int(input('Digite o número final: '))

# Processamento - O programa deve imprimir todos os números de M até N.
for i in range(numero_inicial, numero_final+1):
    # Saída - O programa deve imprimir um número por linha.
    print(i)
