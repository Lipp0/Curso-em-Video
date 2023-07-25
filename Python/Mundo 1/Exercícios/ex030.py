print('--- PAR OU IMPAR ---')
num = int(input('Olá, digite qualquer número inteiro: '))
resto = num % 2

if resto == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))

