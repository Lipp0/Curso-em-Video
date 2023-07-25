nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

média = (nota1 + nota2)/2

if média < 5.0:
    print('REPROVADO')
elif média >= 5.0 and média <= 6.9:
    print('RECUPERAÇÃO')
elif média >= 7.0 and média <= 10.0:
    print('APROVADO')
