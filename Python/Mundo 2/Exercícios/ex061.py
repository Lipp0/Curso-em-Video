primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

ultimo = primeiro + (10-1)*razao
contador = primeiro

while contador <= ultimo:
    print('{}'.format(contador))
    contador += razao