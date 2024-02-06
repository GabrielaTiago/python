
TURTLE = '`0´'
# TURTLE = '''  O
# `( )´
# ´   `
# '''
# TURTLE_R = '''\t  O
# \t`( )´     
# \t´   `     
# '''
# TURTLE_L = '''  O\t
# `( )´\t     
# ´   `\t     
# '''
field = [ TURTLE,'\n', '\n' , '\n', '\n', '\n', '\n', '\n',  '\n', '\n']

def move_turtle():
    sucess = True
    d = ''
    steps = 0

    direction = input('Direção: ')

    if len(direction) > 1:
        print('Digite apenas uma direção por vez!')
        sucess = False
        return sucess
    elif direction == 'q':
        sucess = False
        return sucess
    elif direction == 'w' or direction == '↑':
        d = 'top'
        steps = int(input('Quantos passos? '))
    elif direction == 's' or direction == '↓':
        d = 'bottom'
        steps = int(input('Quantos passos? '))
    elif direction == 'a' or direction == '←':
        d = 'left'
        steps = int(input('Quantos passos? '))
    elif  direction == 'd' or direction == '→':
        d = 'right'
        steps = int(input('Quantos passos? '))
    else:
        print('\nDireção inválida!\n')
        return move_turtle()

    display_field(field, steps, d)
    return sucess


def display_field(field, steps, direction):
    print('-------------------------------------------------------------------------------------------------------------')
    if(direction == 'bottom'):
        for i in range(steps):
            field.insert(0, '\n')
            field.pop()
    if(direction == 'top'):
        for i in range(steps):
            field.append('\n')
            field.pop(0)
    if(direction == 'right'):
        for i in range(len(field) - 1):
            if field[i] == TURTLE:
                for _ in range(steps):
                    field[i] = '  ' + field[i]
                break
    if(direction == 'left'):
        for i in range(len(field) - 1):
            if field[i].find(TURTLE) != -1:
                for _ in range(steps):
                    field[i] = field[i][2:]
                break
    for i in field:
        print(i)
    print('-------------------------------------------------------------------------------------------------------------')

print('Bem vindo(a) ao jogo da tartaruga!\n')
print('Instruções:')
print('\t * Use as teclas "W" ou "↑" para cima e "S" ou "↓" para baixo para movimentar a tartaruga em X')
print('\t * Use as teclas "A" ou "←" para a esquerda ou "D" ou "" para a direita para movimentar a tartaruga em Y')
print('\t * Depois diga a quantidade de passos que a tartaruga deve \'nadar\' em X ou Y.\n')
print('Pressione "Q" para sair do jogo.\n')

while move_turtle():
    pass

print('\nFim do jogo!')
