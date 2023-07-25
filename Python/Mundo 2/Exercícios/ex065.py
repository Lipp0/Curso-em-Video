n2 = 'S'
soma = 0
media = 0
maior = 0
menor = 0
contador = 0

while n2 in 'Ss':
    n1 = int(input('Digite um valor: '))
    soma = soma + n1
    contador = contador + 1
    media = soma / contador
    if contador == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    n2 = input('Quer continuar? [S/N] ').strip().upper()
print('Você digitou {} valores!\nA soma entre eles é {}.\nA média entre eles é {}.\nO maior valor é {} e o menor é {}.'.format(contador, soma, media, maior, menor))