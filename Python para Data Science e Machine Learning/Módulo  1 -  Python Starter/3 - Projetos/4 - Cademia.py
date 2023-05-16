import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 40) if i % 2 == 0]
        self.cabide_halteres = {}
        self.organizar()

    # organizar no cabide
    def organizar(self):
        self.cabide_halteres = {i : i for i in self.halteres}

    #retronar halteres disponiveis
    def disponiveis(self):
        return [i for i in self.cabide_halteres.values() if i != 0]
    
    # pegar o peso e colocar 0 na posição do peso pegado
    def pegarPeso(self, peso):
        peso_posicao = list(self.cabide_halteres.values()).index(peso)
        xave_peso = list(self.cabide_halteres.keys())[peso_posicao]
        self.cabide_halteres[xave_peso] = 0
        return peso
    
    def devolverPeso(self, peso, posicao):
        self.cabide_halteres[posicao] = peso

    def calcularCAOS(self):
        caos = [i for i, j in self.cabide_halteres.items() if i != j]
        return len(caos) / len(self.cabide_halteres)