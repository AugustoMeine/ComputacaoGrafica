import math
import numpy as np

class vetor:
    def __init__(self, valorX, valorY):
        self.valorX = valorX
        self.valorY = valorY
    
    def x(self):
        return(self.valorX)
    
    def y(self):
        return(self.valorY)
    
    def somarVetor(self, valor):
        somarVetorX = self.valorX * valor[0]
        somarVetorY = self.valorY * valor[1]
        print("somarVetor: [",somarVetorX,",",somarVetorY,"]")
        return(np.array((somarVetorX,somarVetorY)))

    def multiplicacaoEscalar(self, valor):
        multiplicarEscalarX = self.valorX * valor
        multiplicarEscalarY = self.valorY * valor
        print("multiplicacaoEscalar: [",multiplicarEscalarX,",",multiplicarEscalarY,"]")
        return(np.array((multiplicarEscalarX,multiplicarEscalarY)))

    def calcularMagnitude(self):
        magnitude = math.sqrt(math.pow(self.valorX,2) + math.pow(self.valorY,2)) 
        print("calcularMagnitude: [",magnitude,"]")
        return(magnitude)

    def calcularVetorUnitario(self):
        magnitude = math.sqrt(math.pow(self.valorX,2) + math.pow(self.valorY,2)) 
        vetorUnitarioX = self.valorX / magnitude
        vetorUnitarioY = self.valorY / magnitude
        print("calcularVetorUnitario: [",vetorUnitarioX,",",vetorUnitarioY,"]")
