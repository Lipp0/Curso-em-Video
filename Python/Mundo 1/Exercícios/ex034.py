print('--- AUMENTOS MÚLTIPLOS ---')
s = float(input('Digite o salário atual: '))

if s <=1250:
    a1 = s + (s*15/100)
    print('O salário teve aumento de R${}'.format(a1))
else:
    a2 = s + (s*10/100)
    print('O salário teve aumento de R${}'.format(a2))

