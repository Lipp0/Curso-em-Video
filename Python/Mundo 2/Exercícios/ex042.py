print('--- ANALISANDO UM TRIÂNGULO ---')
l1 = float(input('Digite o lado 1: '))
l2 = float(input('Digite o lado 2: '))
l3 = float(input('Digite o lado 3: '))

if (l2-l3)<l1 and l1<(l2+l3):
    print('Formou um triângulo...')
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Isóceles!')
    else:
        print('Escaleno!')
else:
    print('Não formou um triângulo.')

