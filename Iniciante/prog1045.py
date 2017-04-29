# -*- coding : utf8 -*-

lados = [float(i) for i in input('').split()]

A,B,C = sorted(lados,reverse=True)

#Classificação dos ângulos
if A >= B + C:
	print('NAO FORMA TRIANGULO')
elif pow(A,2) == (pow(B,2) + pow(C,2)):
	print('TRIANGULO RETANGULO')
elif pow(A,2) > (pow(B,2) + pow(C,2)):
	print('TRIANGULO OBTUSANGULO')
elif pow(A,2) < (pow(B,2) + pow(C,2)):
	print('TRIANGULO ACUTANGULO')

#Classificação dos lados
if A == B == C:
	print('TRIANGULO EQUILATERO')
elif A == B or A == C or B == C:
	print('TRIANGULO ISOSCELES')
