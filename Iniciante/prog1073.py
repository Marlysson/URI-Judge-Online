# -*- coding : utf8 -*-

numero = int(input())

if numero % 2 == 0:
	numero += 1

for n in range(1,numero):
	if n % 2 == 0:
		print("{}^2 = {}".format(n,n**2))
		