from datetime import date

ano_atual= date.today().year
maiores = 0
menores = 0

for _ in range(7):
    ano = int(input('Digite o ano de nascimento: '))
    if (ano_atual - ano) >=18:
        maiores +=1
    else:
        menores+=1
print('{} pessoas atingiram a maior idade, enquanto {} pessoas ainda são menores de idade.'.format(maiores, menores))
