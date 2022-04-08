# Calculadora em Python

print("\n********** CALCULADORA **********")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


while True:
    escolha = input("\nSelecione a operação desejada ou digite N para sair: \n1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão \n \n")

    if escolha == 'N' or escolha == 'n':
        print('Programa Encerrado')
        break

    num1 = int(input("\nDigite o primeiro número: "))
    num2 = int(input("\nDigite o segundo número: "))

    if escolha == '1':
        print("\n")
        print(num1, "+", num2, "=", add(num1, num2))
        print("\n")

    elif escolha == '2':
        print("\n")
        print(num1, "-", num2, "=", subtract(num1, num2))
        print("\n")

    elif escolha == '3':
        print("\n")
        print(num1, "*", num2, "=", multiply(num1, num2))
        print("\n")

    elif escolha == '4':
        print("\n")
        print(num1, "/", num2, "=", divide(num1, num2))
        print("\n")

    else:
        print("\nopção inválida")







