print('Bem vindo(a) ao conversor de moedas!')
r = float(input('Digite o valor em real: '))
d = r/5.24
e = r/5.35
print('O valor R${:.2f} em dólar será US${:.2f} e em euro será ER${:.2f}.'.format(r, d, e))
