# n1 = input("Digite um número: ")
# n2 = input("Digite mais um número: ")
# s = n1 + n2
# print("A soma vale ",s)
# Não irá funcionar porquê o número é considerado uma string, realizando uma concatenação em vez de soma.
# Para funcionar o código, devemos adicionar o tipo primitivo 'int', para converter a string para número inteiro.

# int = 7; -4; 0; 9876;...
# float = 4.5; 0.076; -15.223; 7.0;...
# bool = true; false.
# str = 'olá'; '7.5'; ''.

n1 = int(input('Digite um número: '))
n2 = int(input('digite mais um número: '))
s = n1 + n2
print('A soma de {} e {} vale {}.'.format(n1, n2, s))





