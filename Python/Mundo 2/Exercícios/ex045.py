from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)

print('Suas opções: [0] PEDRA; [1] PAPEL; [2] TESOURA')

jog = int(input('Qual é a sua jogada? '))
print('1...')
sleep(1)
print('2...')
sleep(1)
print('3!')
sleep(2)
print('-='*11)

print(f'Computador jogou: {itens[comp]}')
print(f'Jogador jogou: {itens[jog]}')
print('-='*11)

if comp == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR VENCE!')
    elif jog == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

if comp == 1:
    if jog == 0:
        print('COMPUTADOR VENCE!')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

if comp == 2:
    if jog == 0:
        print('JOGADOR VENCE!')
    elif jog == 1:
        print('COMPUTADOR VENCE!')
    elif jog == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')


