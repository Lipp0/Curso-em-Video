from math import inf
maior_peso = 0
menor_peso = inf

for _ in range(5):
    peso = float(input('Digite o peso em Kg: '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('O menor peso é {}Kg e o maior peso é {}Kg.'.format(menor_peso, maior_peso))
