# Fn = (Fn - 1) + (Fn - 2)
# primeiro termo = 1
# valores iniciais = 1

n = int(input('Digite o termo desejado: '))

F1 = -1
F2 = 1
contador = 1

while contador <= n:
    Fn = F1 + F2
    print(Fn)
    F1 = F2
    F2 = Fn
    contador += 1
print('Fim do programa!')
