# -*- coding : utf8 -*-

numeros = input('').split()
A,B = [int(i) for i in numeros]

if A % B == 0 or B % A == 0:
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')
