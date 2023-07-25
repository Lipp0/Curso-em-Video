sexo = str(input('Olá, digite o seu sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Erro, digite o seu sexo novamente [M/F]: ')).strip().upper()

print('Sexo {} registrado com sucesso!'.format(sexo))