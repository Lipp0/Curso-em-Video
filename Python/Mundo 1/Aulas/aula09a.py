# Cadeia de caracteres/texto (String)

# ex: 'Curso em vídeo Python'
# frase = 'Curso em vídeo Python'
# (Cada caracter da frase, incluindo os espaços, irá ocupar 21 espaços na memória)

# Fatiamento:
# frase[9] -> v
# frase[9:13] -> víde (o 'O' não entrará na lista, pra ele entrar deveria pegar até o 14)
# frase[9:21] -> vídeo Python
# frase[9:21:2] -> (vai do 9 até 21, pulando de 2 em 2)
# frase[:5] -> (o número depois do ':' é onde a frase vai terminar, antes é onde vai começar)
# frase[15:] -> Python (começa no 15 e vai até o final)
# frase[9::3] -> (vai começar no 9 e vai até o final, pulando de 3 em 3)

# Análise:
# len(frase) -> 21 caracteres (len é comprimento)
# frase.count('o', 0, 13) -> 3 (conta quantas vezes aparece a letra 'o', considerando do 0 até 0 12)
# frase.find('deo') -> 11 (em que momento começou o 'deo')
# frase.find('Android') -> -1 (valor que não existe na string)
# 'Curso' in frase -> True

# Transformação:
# frase.replace('Python','Android') -> (substitui 'Python' por 'Adnroid')
# frase.upper() -> (coloca as letras minúsculas em maiúsculas)
# frase.lower() -> (coloca as letras maiúsculas em minúsculas)
# frase.capitalize() -> (joga todos os caracteres em minúsculos, exceto o primeiro caractere)
# frase.title() -> (Analisa as palavras na frase e coloca o primeiro caracter de cada palavra em maiúsculo)
# '   Aprenda Python   ' -> frase.strip() -> (remove os espaços inúteis na string)
# '   Aprenda Python   ' -> frase.rstrip() -> (remove os espaços da direita)
# '   Aprenda Python   ' -> frase.lstrip() -> (remove os espaços da esquerda)

# Divisão:
# frase.split() -> (onde tiver espaço, ele irá criar uma divisão, criando uma lista separando os elementos)

# Junção:
# '-'join(frase) -> (junta todos os elementos da frase e utiliza o '-' para separar as palavras)

