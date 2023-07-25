from time import sleep

print('---- ATIVANDO CONTAGEM REGRESSIVA DE 10 SEGUNDOS PARA A EXPLOSÃO ----')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BOOOOOOM')

