from math import sin, cos, tan
ang = int(input('Digite o ângulo: '))
s = sin(ang)
c = cos(ang)
t = tan(ang)
print('O ângulo {} tem o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(ang, s, c, t))
