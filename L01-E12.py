# Lista 01 - Exercício 12
# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite a altura da pessoa: "))

peso_ideal = (72.7 * altura) - 58

print("A altura ideal é: {}".format(round(peso_ideal, 2)))
