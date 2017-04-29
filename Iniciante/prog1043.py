# -*- coding : utf8 -*-

lados = input('').split()

A,B,C = [float(i) for i in lados]

if abs(A - B) < C  and C < (A + B):
	print('Perimetro = {:.1f}'.format(A+B+C))
else:
	area = ( C * (A + B) ) / 2
	print('Area = {:.1f}'.format(area))
