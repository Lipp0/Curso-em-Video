# CONDIÇÕES ANINHADAS

# carro.siga()
# if carro.esquerda(): -> se (bloco 1)
#   carro.siga()
#   carro.direita()
#   carro.siga()
#   carro.direita()
#   carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
# elif carro.direita(): -> senão se (bloco 2): dentro do If e Else, pode usar quantos quiser
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
# else: -> senão (bloco 3)
#   carro.siga()
# carro.pare()

# Prática:

nome = str(input('Qual é o seu nome? '))
if nome == 'Lippo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

