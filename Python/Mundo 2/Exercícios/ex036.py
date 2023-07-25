print('----- EMPRÉSTIMO BANCÁRIO -----')
print('Olá, bem vindo(a) ao programa de empréstimo bancário!')
valor = float(input('Digite o valor do imóvel desejado: '))
salário = float(input('Agora, digite o seu salário: '))
anos = int(input('Digite a quantidade de anos que será financiado: '))

mês = anos*12
prestação = valor/mês

if prestação > salário*0.3:
    print('O impréstimo não poderá ser realizado, valor da prestação excedido!')
else:
    print('Empréstimo autorizado! O valor da prestação será de R${:.2f}'.format(prestação))
