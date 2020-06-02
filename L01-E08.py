# Lista 01 - Exercício 08
''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês. '''

valor_hora = float(input("Qual o valor da sua hora de trabalho:"))

horas_trabalhadas_mes = float(input("Quantas horas foram trabalhadas no mês"))

salario = horas_trabalhadas_mes * valor_hora

print("O salário por {} horas de trabalho, É de: R$ {}".format(horas_trabalhadas_mes, salario))
