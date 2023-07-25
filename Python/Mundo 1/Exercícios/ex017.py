co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('O triângulo com o cateto oposto {} e cateto adjacente {} tem a hipotenusa {:.2f}.'.format(co, ca, h))
