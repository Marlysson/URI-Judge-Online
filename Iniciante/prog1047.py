
tempo = input('').split()
hora_inicio,minuto_inicio,hora_final,minuto_final = [int(i) for i in tempo]

if hora_final <= hora_inicio:
	tempo = (24 - abs(hora_final - hora_inicio))*60 + minuto_final - minuto_inicio
else:
	tempo = (hora_final - hora_inicio)*60 + (minuto_final - minuto_inicio)

horas = tempo // 60
minutos = tempo - horas*60

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas,minutos))
