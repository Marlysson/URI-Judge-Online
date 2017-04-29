num1 = int(input())
num2 = int(input())

if num1 >= num2:
	maior = num1
	menor = num2
else:
	maior = num2
	menor = num1

s = 0

for num in range(menor+1,maior):
	if num % 2 == 1:
		s += num

print("%d" %s)