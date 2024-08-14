num = int(input('Digite um número: '))
if num>=0:
    fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
    print('O fatorial de', num, 'é', fatorial)
else:
    print('Entrada inválida!')