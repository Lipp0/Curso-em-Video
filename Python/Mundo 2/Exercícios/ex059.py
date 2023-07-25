from time import sleep

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
menu = ('Agora escolha os seguintes números para realizar a operação desejada:\n [1] - Somar\n [2] - Multiplicar\n [3] - maior\n [4] - Novos números\n [5] - Sair do programa')
maior = 0
menor = 0
print(menu)
usuario = int(input('Digite a sua escolha: '))

while usuario != 5:
    if usuario == 1:
        print('Você escolheu Somar! Resultado:\n {} + {} = {}'.format(v1, v2, (v1 + v2)))
        sleep(2)
        print(menu)
        usuario = int(input('Digite sua escolha: '))
    elif usuario == 2:
        print('Você escolheu multiplicação:\n {} x {} = {}'.format(v1, v2, (v1*v2)))
        sleep(2)
        print(menu)
        usuario = int(input('Digite sua escolha: '))
    elif usuario == 3:
        if v1 > v2:
            print('O maior valor é {} e o menor é {}.'.format(v1, v2))
        elif v1 < v2:
            print('O maior valor é {} e o menor é {}.'.format(v2, v1))
        else:
            print('Os dois valores são idênticos!')
        sleep(2)
        print(menu)
        usuario = int(input('Digite sua escolha: '))
    elif usuario == 4:
        novo_v1 = float(input('Digite o novo primeiro valor: '))
        novo_v2 = float(input('Digite o novo segundo valor: '))
        v1 = novo_v1
        v2 = novo_v2
        sleep(2)
        print(menu)
        usuario = int(input('Digite sua escolha: '))

print('Opção 5, programa encerrado!')