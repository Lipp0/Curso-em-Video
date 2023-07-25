numero = int(input('Digite o número desejado: '))
contador = 0
for num in range(1, numero + 1):
    if numero % num == 0:
        contador += 1
if contador == 2:
    print(f'{numero} é primo')
else:
    print(f'{numero} não é primo')
# print('O número {} foi divisível {} vezes'.format(numero, contador))