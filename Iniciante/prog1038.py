# -*- coding:utf-8 -*-

produtos = {
	'1':{'valor': 4},
	'2':{'valor': 4.50},
	'3':{'valor': 5},
	'4':{'valor': 2},
	'5':{'valor': 1.50}
}

codigo , quantidade = input().split()

codigo = str(codigo)
quantidade = int(quantidade)

print("Total: R$ {:.2f}".format( produtos[codigo]["valor"] * quantidade))

