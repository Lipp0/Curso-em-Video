import math

print("Calculadora Científica")

while True:
    print("Selecione a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz quadrada")
    print("7 - Seno")
    print("8 - Cosseno")
    print("9 - Tangente")
    print("10 - Sair")

    op = int(input("Digite sua opção (1-10): "))

    if op == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 + num2)
    elif op == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 - num2)
    elif op == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 * num2)
    elif op == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", num1 / num2)
    elif op == 5:
        num1 = float(input("Digite o número base: "))
        num2 = float(input("Digite o expoente: "))
        print("Resultado: ", num1 ** num2)
    elif op == 6:
        num = float(input("Digite o número: "))
        print("Resultado: ", math.sqrt(num))
    elif op == 7:
        num = float(input("Digite o ângulo em graus: "))
        print("Resultado: ", math.sin(math.radians(num)))
    elif op == 8:
        num = float(input("Digite o ângulo em graus: "))
        print("Resultado: ", math.cos(math.radians(num)))
    elif op == 9:
        num = float(input("Digite o ângulo em graus: "))
        print("Resultado: ", math.tan(math.radians(num)))
    elif op == 10:
        print("Obrigado por utilizar a calculadora científica!")
        break
    else:
        print("Opção inválida. Tente novamente.")