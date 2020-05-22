# Lista 01 - Exercício 11
'''
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

a = (numero_inteiro1 * 2) * (numero_inteiro2 / 2)
b = (numero_inteiro1 * 3) + numero_real
c = (numero_real ** 3)

print("a) Resultado: {}".format(a))
print("b) Resultado: {}".format(b))
print("c) Resultado: {}".format(c))
