# -*- coding:utf-8 -*-

pares,impares,positivos,negativos = 0,0,0,0

for _ in range(5):
	num = int(input())

	# if num % 2 == 0:
	# 	pares += 1
	# else:
	# 	impares += 1

	# if num > 0:
	# 	positivos += 1
	# else:
	# 	negativos += 1

pares = len([numero for numero in ])
print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivos))
print('{} valor(es) negativo(s)'.format(negativos))