# Medidor de velocidade

# Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua.
# Crie um programa que recebe do usuário um valor que representa a velocidade.
# Com base nessa velocidade diga: se ela tomou um multa leve, grave ou gravissima.
#  - Se a pessoa estiver abaixo da velocidade máxima, deve exibir: "Não houve multa",
#  - Caso esteja até 10km acima, deve exibir: "Levou multa leve",
#  - Caso esteja eentre 11km a 20km acima da velocidade máxima, exibir: "Levou multa grave",
#  - Caso esteja acima de 20km acima da velocidade máxima, exiba: "Levou multa gravissima"

MAX_SPEED = 80
result = ''

# Entrada - Recebe a velocidade do carro.
speed = int(input('Digite a velocidade do carro: '))

velocity_serious_fine = MAX_SPEED + 10
velocity_serious_plus_fine = MAX_SPEED + 20

# Processamento - Calcula a multa.
if speed > MAX_SPEED:
   # aqui tem multa ver o qual tipo
   if(speed <= velocity_serious_fine):
        result = 'Levou multa leve'
   elif(speed > velocity_serious_fine and speed <= velocity_serious_plus_fine):
       result = 'Levou multa grave'
   elif(speed > velocity_serious_plus_fine):
       result = 'Levou multa gravissima'
else:
    result = 'Não houve multa.'

# Saída - Imprime o resultado.
print(result)