num = int(input('Digite um número qualquer para saber seu fatorial: '))

contador = num
f = 1

print('Calculando {}!: '.format(num), end="")

while contador > 0:
    print('{}'.format(contador), end="")
    f *= contador
    contador -= 1
    print(' x ' if contador >= 1 else ' = ', end="")
print('{}'.format(f))
