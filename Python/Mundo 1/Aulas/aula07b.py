# Exemplos:

# pow(4,3) = 64
# 81**(1/2) = 9.0
# 25**(1/2) 5.0
# 127**(1/3) = 5.026525695313479
# 'oi' + 'olá' = 'oiolá'
# 'oi'*5 = 'oioioioioi'
# '='*20 = '===================='
# print('='*20) = ====================

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))

# Se colocar ':20' entre os colchetes, o caractere será escrito em 20 espaços.
# Para realizar o alinhamento, poderá ser colocado entre ':20' o sinal de maior (>) para alinhar a direita, sinal de menor (<) para alinhar a esquerda ou acento circunflexo (^) para centralizar.
# Colocando o sinal de igual entre os dois pontos e o sinal de alinhamento, o sinal de igual preencherá os espaços do caractere (:=^20).

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}.'.format(n1+n2))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end='')
print('A divisão inteira é {} e a potência é {}.'.format(di, e))

# ':.3f' serve para limitar o número de casas decimais após a vírgula
# "end=''" serve para continuar a linha. O que for colocado nas aspas, será acrescentado entre uma linha e outra
# '\n' serve para "quebrar" a linha
