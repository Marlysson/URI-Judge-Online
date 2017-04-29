# -*- coding:utf-8 -*-

numeros = []

for i in range(5):
	numeros.append(float(input()))

pares = [i for i in numeros if i % 2 == 0]

print('{} valores pares'.format(len(pares)))