# REGEX
# Regular Expressions

# Metacaracteres
# [] - Um conjunto de caracteres
# \ - Sinaliza uma sequência especial (também pode ser usado para escapar de metacaracteres)
# . - Qualquer caractere (exceto caractere de nova linha)
# ^ - Começa com
# $ - Termina com
# * - Zero ou mais ocorrências
# + - Uma ou mais ocorrências
# {} - Exatamente o número especificado de ocorrências
# | - Ou
# () - Captura e agrupa


import re

# re.search() - retorna um objeto match se encontrar a primeira ocorrência
# re.findall() - retorna uma lista contendo todas as ocorrências
# re.sub() - substitui todas as ocorrências de uma string
# re.split() - divide a string onde encontrar a ocorrência

# Exemplo 1
text = 'The rain in Spain'
x = re.search('^The.*Spain$', text)
if x:
    print('Encontrou')
else:
    print('Não encontrou')

# Exemplo 2

x = re.findall('ai', text)
print(x)

# Exemplo 3

x = re.sub('ai', '123', text)
print(x)

# Exemplo 4

x = re.split('ai', text)
print(x)



