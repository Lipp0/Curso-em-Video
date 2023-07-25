primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

contador = 1
termo = 0
usuario = -1
tamanho = 10

while True:
    while contador < tamanho:
        termo += razao
        contador += 1
        print(termo)
    usuario = int(input('Mais termos? Digite 0 para finalizar o programa: '))
    if usuario == 0:
        break
    usuario += contador
    tamanho = usuario
print('FIM DO PROGRAMA!')
