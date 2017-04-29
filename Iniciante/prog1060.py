# -*- coding :utf8 -*-

numeros = []

for i in range(6):
	numero = float(input())
	numeros.append(numero)


positivos = len([i for i in numeros if i > 0])

print('{} valores positivos'.format(positivos))