carros = [
    ([1], "Chevrollet Tracker", 120),
    ([2], "Chevrollet Spin", 150)
    ([3], "Fiat Uno", 50)
    ([4], "Fiat Siena", 80)
    ([5], "Renout Sandero", 100)
    ([6], "Renout Duster", 180)
    ]
alugados = []


def mostrar_listagem_de_veiculos(lista_de_veiculos):
    for i, car in enumerate(lista_de_veiculos):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car [1]))



while True:
    
    print("Bem vindo à Locadora de Carros!")
    print("O que deseja fazer?")
    print("0 - Mostrar Portifólio | 1 - Alugar um veículo | 2 - Devolver um veículo")
    op = int(input())

  
    if op == 0:
        mostrar_listagem_de_veiculos(carros)

    elif op == 1:
        mostrar_listagem_de_veiculos(carros)
        cod_car = int(input())
        print("Por quantos dias você deseja ficar com o veículo? ")
        dias = int(input())
        

        print("Você optou por {} por {} dias.".format(carros[cod_car][0]))
        print("O aluguel total será R$ {}. Deseja realmente alugar?".format(dias * carros[cod_car][1]))

        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print(" Ok, você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não existe carros para devolver.")
        else:
            print(" Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_listagem_de_veiculos(alugados)
            print("Escolha o código do carro que deseja devolver: ")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o veículo {}.".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    print(" Digite 0 para CONTINUAR | 1 para SAIR")
    if float(input()) == 1:
        break