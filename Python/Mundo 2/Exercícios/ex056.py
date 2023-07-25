soma = 0
media = 0
maior = 0
velho = ''
total = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = input('NOME: ').strip()
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M/F]: ').strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        velho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        velho = nome
    if sexo in 'Ff' and idade < 20:
        total += 1

media = soma/4

print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total))
