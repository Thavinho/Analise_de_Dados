import random
import os

class JogoDaVelha:
    def __init__(self):
        self.reset()

    def print_tabuleiro(self):
        print("")
        print(" " +  self.tabuleiro[0][0] + " | " + self.tabuleiro [0][1] + " | " + self.tabuleiro[0][2])
        print("----------")
        print(" " +  self.tabuleiro[1][0] + " | " + self.tabuleiro [1][1] + " | " + self.tabuleiro[1][2])
        print("----------")
        print(" " +  self.tabuleiro[2][0] + " | " + self.tabuleiro [2][1] + " | " + self.tabuleiro[2][2])

    def reset(self):
        self.tabuleiro = [["", "","",],["","","",],["","",""]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X", "O"]:
            # Horizontais
            dict_win[1] = (self.tabuleiro [0][0] == self.tabuleiro [0][1] == self.tabuleiro [0][2] == i)
            dict_win[1] = (self.tabuleiro [1][0] == self.tabuleiro [1][1] == self.tabuleiro [1][2] == i) or dict_win[i]
            dict_win[1] = (self.tabuleiro [2][0] == self.tabuleiro [2][1] == self.tabuleiro [2][2] == i) or dict_win[i]
    
            # Verticais
            dict_win[1] = (self.tabuleiro [0][0] == self.tabuleiro [1][0] == self.tabuleiro [2][0] == i) or dict_win[i]
            dict_win[1] = (self.tabuleiro [0][1] == self.tabuleiro [1][1] == self.tabuleiro [2][1] == i) or dict_win[i]
            dict_win[1] = (self.tabuleiro [0][2] == self.tabuleiro [1][2] == self.tabuleiro [2][2] == i) or dict_win[i]

            #Diagonais
            dict_win[1] = (self.tabuleiro [0][0] == self.tabuleiro [1][1] == self.tabuleiro [2][2] == i) or dict_win[i]
            dict_win[1] = (self.tabuleiro [2][0] == self.tabuleiro [1][1] == self.tabuleiro [0][2] == i) or dict_win[i]

        if dict_win["X"]:
            self.done = "x"
            print("X Venceu!")
            return
        elif dict_win["O"]:
            self.done = "o"
            print("O Venceu!")
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != "":
                    c += 1
                    break

    def jogada_jogador(self):
        modo_invalido=True
        while modo_invalido:
            try:
                print("Digite a linha do seu próximo lance: ")
                x = int(input())
                print("Digite a coluna do seu próximo lance: ")
                y = int(input())
                if x > 2 or x < 0 or y > 2 or y < 0:
                    print("Coordenadas Invalidas - ")
                
                if self.tabuleiro [x] [y] != " ":
                    print("Posição já preenchida.")
                    continue
            except Exception as e:
                print(e)
                continue

        modo_invalido = False
        self.tabuleiro[x][y] = "X"

    def fazer_jogada(self):
        jogadas_possiveis = []

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    jogadas_possiveis.append((i,j))

        if len(jogadas_possiveis) > 0:
                    x, y = random.choice(jogadas_possiveis)
                    self.tabuleiro[x][y] = "0"        

self = JogoDaVelha()
self.print_tabuleiro()
next = 0

