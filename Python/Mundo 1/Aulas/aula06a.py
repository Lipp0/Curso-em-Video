# print(type(x)) mostra qual o tipo primitivo do valor 'x'.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
print("A soma entre {} e {} vale {}.".format(n1, n2, s))
# print("A soma entre", n1, "e", n2, "vale", s) está certo, porém utiliza muito da vírgula e áspas (sintaxe antiga).