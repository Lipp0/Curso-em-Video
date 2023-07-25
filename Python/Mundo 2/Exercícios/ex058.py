from random import randint
from time import sleep

computador = randint(0, 10)
r2 = 0
palpites = 0

print('--- JOGO DA ADIVINHAÇÃO ---')
r1 = str(input(('Olá usuário, quer brincar de advinhação [S/N]? '))).strip().upper()
if r1 == 'S':
    print('Okay vamos jogar! Estou pensando em um número de 0 a 10...')
    sleep(3)
    while r2!= computador:
        r2 = int(input('E aí, sabe qual número é? '))
        palpites += 1
        if r2 == computador:
            print('ACERTOOOU! Você tentou {} palpites.'.format(palpites))
        else:
            print('ERROOOU!Tente novamente.')
else:
    print('Poxa... Então deixa pra depois!')
print('Fim do jogo!')
