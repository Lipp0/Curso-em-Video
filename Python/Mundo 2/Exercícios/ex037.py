num = int(input('Digite qualquer número inteiro: '))
base = int(input('Agora digite 1 para base binária, 2 para base octal e 3 para base hexadecimal: '))

if base == 1:
    print('O número {} em binário fica'.format(num),bin(num))
elif base == 2:
    print('O número {} em octal fica'.format(num),oct(num))
else:
    print('O número {} em hexadecimal fica'.format(num),hex(num))