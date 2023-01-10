import os
print ('_____')
operation = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",}

while True:
    os.system("clear")
    i = 0
    for op, name in operation.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operação que deseja realizar em seguida: ")
    op = input()
    op_string = list(operation.keys())[int(op)]

    print("")
    print(">>> {} escolhida.".format(op_string))
    print("")
    print("Qual o primeiro número? ")
    v1 = float(input())
    print("Qual o segundo número? ")
    v2 = float(input())

    if op == '0':
        resultado = v1 + v2
    elif op == '1':
        resultado = v1 - v2
    elif op == '2':
        resultado = v1 * v2
    elif op == '3':
        resultado = v1 / v2

    print("")
    print(" {} {} {} = {}".format(v1, op_string, v2, resultado))
    print("")

    print("Deseja realizar mais alguma operação? (Digite 1 para sair ou 2 para continuar) ")
    comando = int(input())
    if float(input()) == 1:
        break
