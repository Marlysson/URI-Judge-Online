# -*- coding:utf8 -*-

numeros = []
testes = int(input())

for i in range(testes):
	numero = int(input())
	numeros.append(numero)

for numero in numeros:

	if numero == 0:
		print('NULL')
	else:
		
		if numero % 2 == 0:
			print('EVEN ',end="")
		else:
			print('ODD ',end="")
			
		if numero > 0:
			print('POSITIVE')
		else:
			print('NEGATIVE')
	