produto = float(input('Digite o valor do produto: '))
pag = int(input('Digite 1 para pagamento à vista no dinheiro/cheque, 2 para pagamento à vista no cartão, 3 em até 2x no cartão ou 4 para 3x ou mais no cartão: '))

if pag == 1:
    desc1 = (produto * 10)/100
    print('À vista no dinheiro/cheque você recebe um desconto de 10%, saindo por R${}'.format(desc1))
elif pag == 2:
    desc2 = (produto * 5)/100
    print('À vista no cartão você recebe um desconto de 5%, saindo por R${}'.format(desc2))
elif pag == 3:
    print('Pagando 2x no cartão você não receberá desconto.')
elif pag == 4:
    juros = (produto*20)/100
    print('Dividindo de 3x ou mais no cartão, o valor do produto sairá por R${}'.format(juros))
