# Lista 01 - Exercício 04
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = float(input("Digite a primeira nota do bimestre:"))
segunda_nota = float(input("Digite a segunda nota do bimestre:"))
terceira_nota = float(input("Digite a terceira nota do bimestre:"))
quarta_nota = float(input("Digite a quarta nota do bimestre:"))

media_bimestre = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"A média no bimestre foi: {media_bimestre}")
