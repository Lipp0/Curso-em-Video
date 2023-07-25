# ESTRUTURA DE REPETIÇÃO FOR

# laço C no intervalo(1,10) -> for c in range(1,10)
#   passo
# pega

# laço c no intervalo(0,3) -> for c in range(0,3)
#   passo
#   pula
# passo
# pega

# laço c no intervalo(0,3) -> for c in range(0,3)
#   se moeda               -> if moeda:
#       pega
#   passo
#   pula
# passo
# pega

# Prática:

for c in range(1, 7):
    print('oi')
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')

i = int(input('início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
