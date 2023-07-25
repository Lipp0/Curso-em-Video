# Condições If e Else

# carro.siga()
# se carro.esquerda() -> bloco verdadeiro
#    carro.siga()
#    carro.direita()
#    carro.esquerda()
#    carro.siga()
#    carro.direita()
#    carro.siga()
# senão               -> bloco falso
#    carro.siga()
#    carro.esquerda()
#    carro.siga()
#    carro.esquerda()
#    carro.siga()
# carro.pare()

# Condição:

# if carro.esquerda():
#     bloco True
# else:
#     bloco False

# Exemplo:

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('---FIM---')

#print('Carro novo!' if tempo <=3 else 'Carro velho!') -> versão simplificada
