# -*- coding:utf8 -*-

valor_total = int(input())

cedulas = [100,50,20,10,5,2,1]

print(valor_total)

for i in cedulas:
	valor = valor_total // i
	valor_total -= valor * i

	print("{} nota(s) de R$ {:.2f}".format(valor,i))