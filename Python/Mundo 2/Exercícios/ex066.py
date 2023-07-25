soma = cont = 0
while True:
    valor = int(input('Digite um valor, caso queira parar digite 999: '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'A soma dos {cont} valores foi {soma}!')