print('--- ANALISANDO UM TRIÂNGULO ---')
l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

if (l2-l3)<l1 and l1<(l2+l3): # if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Formou um triângulo!')
else:
    print('Não formou um triângulo.')
