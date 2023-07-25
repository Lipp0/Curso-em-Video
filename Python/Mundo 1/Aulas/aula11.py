# representar uma cor em python: \033[style;text;backm

# Style -> 0 (sem estilo), 1 (negrito), 4 (sublinhado)e 7 (inverte as configurações).
# Text -> 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul escuro), 35 (roxo), 36 (azul claro) e 37 (cinza).
# Back -> 40 (branco), 41 (vermelho), 42 (verde), 43 (amarelo), 44 (azul escuro), 45 (roxo), 46 (azul claro) e 47 (cinza).

# Ex: \033[0;33;44m , \033[0;30;41m , \033[4;33;44m , \033[7;30m (letra preta e fundo branco)

# prática:

print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mEstou trocando as cores!\033[m') # -> o '\033[m' no final limita a cor
print('\033[7;33;44mPython é vida!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{}!\033[m'.format(a, b))
nome = 'Michel'
print('Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores ={'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;32;m'}
print('Olá pequeno gafanhoto! seu nome é {}{}{}? Show!'.format(cores['pretoebranco'], nome, cores['limpa']))

