soma = 0
# cont = 0
for _ in range(6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        # cont += 1
print('A soma dos números pares é {}.'.format(soma))
