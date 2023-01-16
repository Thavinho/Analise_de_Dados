import random
import os

movimento = ["pedra", "papel", "tesoura"]
jogador = 0
computador = 0

print("Bem vindo ao jogo Pedra, Papel e Tesoura")

def main_print():
    print("\nPLACAR:")
    print("Jogador: {}".format(jogador))
    print("Computador: {}".format(computador))
    print("\n")
    print("Escolha sua jogada:")
    print("0 - PEDRA | 1 - PAPEL | 2 - TESOURA")

def select_move():
    return random.choice(movimento)

def player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return movimento[player_move]
        except Exception as e:
            print(e)

def winner(p_move, c_move):
#Papel
    if p_move == 'papel:':
        if c_move == 'pedra':
            jogador += 1
        return "p"
    elif c_move == 'tesoura':
        computador += 1
        return "c"
    else:
        return "d"
#Pedra
    if p_move == 'pedra:':
        if c_move == 'tesoura':
            jogador += 1
        return "p"
    elif c_move == 'papel':
        computador += 1
        return "c"
    else:
        return "d"
#Tesoura
    if p_move == 'tesoura:':
        if c_move == 'papel':
            jogador += 1
        return "p"
    elif c_move == 'pedra':
        computador += 1
        return "c"
    else:
        return "d"

again = 1
while again == 1:
    main_print()
    jogador = player_move
    computador = select_move
    win = winner(jogador, computador)

    print("Sua Jogada: {}".format(player_move.upper()))
    print("Jogada do Computador: {}".format(computador.upper()))

    if win == "p":
        print("Você venceu!")
    elif win == "c":
        print("Você perdeu!")
    else:
        print("Empate!")

    while True:
        print(" Deseja jogar novamente? 0 - SIM | 1 - NÃO")
        if next == 0:
            break
        elif next == 1:
            again == 0
            break
