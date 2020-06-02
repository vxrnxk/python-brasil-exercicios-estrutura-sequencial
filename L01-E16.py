# Lista 01 - Exercício 16
'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

area_a_ser_pintada = float(input("Digite quantos metros quadrados serão pintados? "))

litros_tinta = area_a_ser_pintada / 3.0
quantidade_latas = int(litros_tinta / 18.0)

if(litros_tinta % 18.0 != 0):
    quantidade_latas += 1

print(f"Quantidade de latas: { quantidade_latas }")
print(f"Valor a ser pago pela tinta: R$ { quantidade_latas * 80 }")