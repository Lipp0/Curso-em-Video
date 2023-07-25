P = float(input('Olá, digite o preço do produto: '))
D = P*(5/100)
print('O produto com preço R${:.2f} obteve um desconto de 5%, alterando o preço para R${:.2f}.'.format(P, D))
