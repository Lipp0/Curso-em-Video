print('--- RADAR ELETRÔNICO ---')
vel = int(input('Olá, digite a velocidade do carro em Km: '))
if vel <= 80:
    print('Parabéns, você está no limite de velocidade!')
else:
    m = 7*(vel-80)
    print('EI! Você está acima do limite, será multado no valor de R${},00.'.format(m))
print('Dirija com segurança!')
