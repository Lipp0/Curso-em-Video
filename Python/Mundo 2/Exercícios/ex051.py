primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

ultimo = primeiro + (10-1)*razao

for c in range(primeiro, ultimo+razao, razao):
    print(c)