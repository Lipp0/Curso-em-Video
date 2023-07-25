print('--- CUSTO DA VIAGEM ---')
v = float(input('Olá, digite a distância da viagem em Km: '))
if v <= 200:
    p1 = v*0.50
    print('O custo da viagem com a distância de {}Km fica de R${}'.format(v, p1))
else:
    p2 = v*0.45
    print('O custo da viagem com a distância de {}Km fica de R${}'.format(v, p2))

