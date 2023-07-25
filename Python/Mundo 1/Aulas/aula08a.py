# Bibliotecas de importações:

# Ex:
# import math (importa todas as funcionalidades da biblioteca)
# from math import pow (importa apenas a funcionalidade que eu escolher da biblioteca)

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, math.ceil(raiz)))
# ceil arredonda para cima.

