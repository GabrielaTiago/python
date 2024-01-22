# Problema 1 - Valor por hora
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

# Entrada
# O programa deve receber dois números inteiros, o primeiro representa o salário mensal do funcionário e o segundo o número de horas trabalhadas por mês.
salario_mensal = int(input('Digite o salário mensal: '))
horas_trabalhadas = int(input('Digite o número de horas trabalhadas por mês: '))

valor_hora = salario_mensal / horas_trabalhadas

# Saída
# O programa deve imprimir o valor da hora trabalhada com duas casas decimais.
print(f'O valor da hora trabalhada é de R$ {valor_hora:.2f}')
