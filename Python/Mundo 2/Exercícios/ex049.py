print('Olá, bem vindo(a) a tabuada de multiplicação!')
número = int(input('Digite o número desejado: '))

for multiplicador in range(1,11):
    print('{} X {} = {:2}'.format(número, multiplicador, número * multiplicador))

