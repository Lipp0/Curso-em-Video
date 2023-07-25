ano = int(input('Digite o ano do seu nascimento: '))
idade = 2022 - ano

if idade <= 9:
    print('MIRIM')
elif idade >= 10 and idade <= 14:
    print('INFANTIL')
elif idade >=15 and idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')



