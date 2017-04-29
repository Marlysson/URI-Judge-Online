# -*- coding :utf8 -*-

numeros = []

for i in range(6):
	numero = float(input())
	numeros.append(numero)

positivos = [numero for numero in numeros if numero > 0]

print('{} valores positivos'.format(len(positivos)))
print('{:.1f}'.format(float(sum(positivos)/len(positivos))))