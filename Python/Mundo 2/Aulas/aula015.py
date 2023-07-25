# INTERRROMPENDO REPETIÇÕES WHILE

# while true:
#   if chão:
#       passo
#   if espaço:
#       pula
#   if moeda:
#       pega
#   if trofeu:
#       pula
#       break -> interrompe o loop e sai do laço de repetição
# pega

# PRÁTICA

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print (f'A soma vale {s}') # python 3.6+
