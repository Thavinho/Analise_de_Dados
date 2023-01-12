import random

class Gym:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_alteres = {}
        self.reiniciar_dia()

    def reiniciar_dia(self):
        self.porta_alteres = {i: i for i in self.halteres}

    def listagem_halteres(self):
        return [i for i in self.porta_alteres.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.porta_alteres.itens() if j == 0]

    def take_halteres(self, peso):
        halt_pos = list(self.porta_alteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso

    def return_halteres(self, pos, peso):
        self.porta_alteres[pos] = peso


    def calcular_caos(self):
        num_caos = [i for i, j in self.porta_alteres.itens() if i != j]
        return len(num_caos) / len(self.porta_alteres)

    
class Usuarios:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_peso = self.academia.listagem_halteres()
        self.peso = random.choice(lista_peso)
        self.academia.take_halteres(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_halteres()

        if self.tipo == 1:
                if self.peso in espacos:
                    self.academia.return_halteres(pos, self.peso)
                else:
                    pos = random.choice(espacos)
                    self.academia.return_halteres(pos, self.peso)

        if self.tipo == 2:
            pos = random.choice(espacos)
            self.academia.return_halteres(pos, self.peso)
        self.peso = 0
        
academia = Gym()

usuarios = [Usuarios(1, academia) for i in range (10)]
usuarios += [Usuarios(2, academia) for i in range (1)]
random.shuffle(usuarios)

list_chaos = []

for k in range[50]:
    academia.reiniciar_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_chaos += [ academia.calcular_caos()]
        
academia.porta_alteres
academia.calcular_caos()



self = Gym()