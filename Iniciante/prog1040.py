# -*- coding:utf-8 -*-


notas = list(map(float,input().split()))
pesos = [2.0,3.0,4.0,1.0]

soma_por_pesos = sum(nota * peso for nota , peso in zip(notas,pesos))
media = soma_por_pesos / sum(pesos)

print('Media: %.1f' % media)

if media >= 7.0:
	print('Aluno aprovado.')

elif media < 5.0:
	print('Aluno reprovado.')

elif 5.0 <= media <= 6.9:
	
	print('Aluno em exame.')

	nota_exame = float(input())

	print("Nota do exame: %.1f" %nota_exame)

	media = ( nota_exame + media ) / 2

	if media >= 5:
		print('Aluno aprovado.')
	else:
		print('Aluno reprovado.')

	print('Media final: %.1f' % media)
