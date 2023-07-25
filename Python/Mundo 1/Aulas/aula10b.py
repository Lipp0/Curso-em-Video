# Exemplos:

print('--- EXEMPLO 1 ---')
nome = str(input('Qual é o seu nome? '))
if nome == 'Michel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}'.format(nome))

print('---EXEMPLO 2 ---')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m >= 6.0:
    print('Passou, BOA MLK!')
else:
    print('Pegou recuperação, VAI ESTUDAR MEU NOBRE!')
print('-'*12)
