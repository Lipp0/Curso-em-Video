ano = int(input('Digite seu ano de nascimento: '))
idade = 2022 - ano
t = idade - 18

if idade < 18:
    print('Ainda não é seu ano de alistamento, faltam {} anos!'.format(t))
elif idade == 18:
    print('Esse ano você deve se alistar!')
else:
    print('O seu ano já passou fazem {} anos!'.format(t))
