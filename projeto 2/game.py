from turtle import Turtle

# Constants
STEPS_PROMPT = 'Quantos passos? '
DEGREES_PROMPT = 'Quantos graus? '
NEW_ATTEMPT = 'Nova tentativa: '
NUMBERS_ONLY = 'Digite apenas números inteiros!'
ONE_LETTER_ONLY = 'Digite apenas uma letra por vez para representar a direção!'
WRONG_DIRECTION = '\nDireção inválida!'

# Initialize the turtle
t = Turtle()
t.shape('turtle')
t.color('green')
t.left(90)
t.speed(4)

# Functions
def checks_the_input_size(direction: str):
    if len(direction) > 1:
        print(ONE_LETTER_ONLY)
        direction = input(NEW_ATTEMPT).lower()
    return direction

def get_steps():
    try:
        steps = int(input(STEPS_PROMPT))
    except ValueError:
        print(NUMBERS_ONLY)
        steps = int(input(STEPS_PROMPT))
    return steps

def get_degrees():
    try:
        degrees = int(input(DEGREES_PROMPT))
    except ValueError:
        print(NUMBERS_ONLY)
        degrees = int(input(DEGREES_PROMPT))
    return degrees

def rotate_turtle():
    direction_left_or_right = input('\n["D", "E"]  Você deseja ir para esquerda ou direita? ').lower()
    direction_left_or_right = checks_the_input_size(direction_left_or_right)

    if direction_left_or_right == 'e' or direction_left_or_right == 'd':
        if direction_left_or_right == 'e':
            degrees = get_degrees()
            t.left(degrees)
        elif  direction_left_or_right == 'd':
            degrees = get_degrees()
            t.right(degrees)
    else:
        print(WRONG_DIRECTION)

# Game the instructions
print('Bem vindo(a) ao mini game da tartaruga!\n')
print('Instruções:')
print('\t * Use as teclas "F" para frente e "T" para trás para movimentar a tartaruga em X')
print('\t * Use as teclas "E  para a esquerda e "D" para a direita para movimentar a tartaruga em Y')
print('\t * Depois diga a quantidade de passos que a tartaruga deve \'nadar\' em X ou Y.\n')

# Game loop
while True:
    direction_back_or_forward = input('\n["F", "T"] Você deseja ir para frente ou para trás? ').lower()
    direction_back_or_forward = checks_the_input_size(direction_back_or_forward)

    if direction_back_or_forward == 'f' or direction_back_or_forward == 't':
        if direction_back_or_forward == 'f':
            steps = get_steps()
            rotate_turtle()
            t.forward(steps)
        elif direction_back_or_forward == 't':
            steps = get_steps()
            rotate_turtle()
            t.backward(steps)
            # t.left(180)
    else:
        print(WRONG_DIRECTION)

    keep_playing = input('\nDeseja continuar jogando? [S/N] ').lower()

    if keep_playing.startswith('n'):
        break
    elif keep_playing.startswith('s'):
        continue
    else:
        print('\nOpção inválida! Encerrando o jogo...')
        break

print('\nObrigado(a) por jogar!')