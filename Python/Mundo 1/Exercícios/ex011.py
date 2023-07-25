L = float(input('Olá,digite a largura da parede em metros: '))
H = float(input('Agora digite a altura em metros: '))
A = L*H
# cada litro de tinta equivale a 2m²
T = A/2
print('A parede que tem a largura em {}m e altura em {} possui a área em {}m². A quantidade de tinta necessária é de {}L.'.format(L,H,A,T))
