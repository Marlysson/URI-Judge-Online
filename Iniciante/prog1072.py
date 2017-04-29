vezes = int(input())

dentro,fora = 0,0

for i in range(vezes):

	numero = int(input())

	if 10 <= numero <= 20:
		dentro += 1
	else:
		fora += 1
		
print('{} in'.format(dentro))
print('{} out'.format(fora))
