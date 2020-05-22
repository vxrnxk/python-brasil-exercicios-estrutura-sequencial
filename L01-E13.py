# Lista 01 - Exercício 13
'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

import sys

altura = float(input("Digite a altura da pessoa: "))
sexo = raw_input("Digite o sexo: ")

if sexo == "h":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "m":
    peso_ideal = (62.1 * altura) - 44.7
else:
    sys.exit("Digite um sexo válido!")

print("O peso ideal é: {}".format(peso_ideal))
