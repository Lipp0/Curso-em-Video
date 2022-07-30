Km = float(input('Digite quantos Km rodados o carro percorreu: '))
D = int(input('Digite a quantidade de dias que o carro foi alugado: '))
P = (60*D)+(0.15*Km)
print('O valor total a pagar pelo aluguel do carro é de R${:.2f}.'.format(P))
