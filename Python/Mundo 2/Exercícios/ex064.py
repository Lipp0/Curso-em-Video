# flag = 999
soma = 0
contador = 0

while True:
    num = int(input('Digite um número inteiro (digite 999 para finalizar): '))
    if num != 999:
        soma += num
        contador += 1
    else:
        print('Finalizando o programa.')
        break
print('Foram digitados {} números e o resultado da soma entre eles é {}.'.format(contador, soma))
