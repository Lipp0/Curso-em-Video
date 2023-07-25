# ESTRUTURA DE REPETIÇÃO WHILE

# while not _ : -> enquanto não
#   passo
# pega

# while not maçã:
#   if chão:
#       passo
#   if espaço:
#       pula
#   if moeda:
#       pega
# pega

# PRÁTICA:

'''for c in range (1, 10): -> usado só quando se sabe o limite
    print(c)
print('Fim')'''

c = 1
while c < 10:
    print(c)
    c = c+1
print('Fim')

print('-'*10)

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

print('-'*10)

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

