from random import randint
from time import sleep # simula o computador 'pensando'
computador = randint(0, 5) # faz o computador 'pensar'

print('--- JOGO DA ADIVINHAÇÃO ---')
r1 = str(input(('Olá usuário, quer brincar de advinhação (Sim/Não)? ')))
if r1 == 'Sim':
    print('Okay vamos jogar! Estou pensando em um número de 0 a 5...')
    sleep(3)
    r2 = int(input('E aí, sabe qual número é? '))
    if r2 == computador:
        print('Acertou mizeravi!')
    else:
        print('ERROOOOOU! Pensei no número {}.'.format(computador))
else:
    print('Poxa... Então deixa pra depois!')
print('Fim do jogo!')
