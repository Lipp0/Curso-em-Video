# from datetime import date
# date.today().year -> para analizar o ano atual

print('--- ANO BISSEXTO ---')
ano = int(input('Digite o ano desejado: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
