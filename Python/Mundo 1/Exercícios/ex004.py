x = input('digite algo: ')
print('O tipo primitivo desse valor é {}.'. format(type(x)))
print('Só tem espaços? {}.'.format(x.isspace()))
print('É letra? {}.'.format(x.isalpha()))
print('É número? {}.'.format(x.isnumeric()))
print('É alfanumérico? {}.'.format(x.isalnum()))
print('Está em maiúsculo? {}.'.format(x.isupper()))
print('Está em minúsculo? {}.'.format(x.islower()))
print('Está capitalizada? {}'.format(x.istitle()))
print('É decimal? {}.'.format(x.isdecimal()))