# Fatorial de um número

# Entrada - Rcebe um número inteiro.
number = int(input('Digite um número: '))
text = ''

#  Processamento - Calcula o fatorial do número.
fatorial = 1
if number < 0:
    text = 'Não existe fatorial de número negativo.'
elif number == 0 | number == 1:
    text = f'O fatorial de {number} é 1.'
else:
    number_copy = number
    while number_copy > 1:
        fatorial = number_copy * fatorial
        number_copy -= 1
    text = f'O fatorial de {number} é {fatorial}.'

# Saída - Imprime o fatorial do número.
print(text)