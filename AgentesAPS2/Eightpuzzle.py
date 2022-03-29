from os import stat
from turtle import right
from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import AEstrela
from Graph import State
import copy
import numpy as np


class Eightpuzzle (State):
    
    def __init__(self, estado, op, posi, posj):
        self.operator = op
        self.estado = estado
        self.i = posi
        self.j = posj
        self.objetivo = np.array([[1,2,3],[8,0,4],[7,6,5]])
        self.correctPos = [[0,2,2],[1,1,1],[2,1,2],[3,1,3],[4,2,3],[5,3,3],[6,3,2],[7,3,1],[8,2,1]]

    def isSolvable(self):
       invCount = self.getInvCount()
       return (invCount % 2 == 0)



    def getInvCount(self):
        lista = self.estado.flatten()
        dict_ideal = {1:0,2:1,3:2,8:3,0:4,4:5,7:6,6:7,5:8}
        sum = 0
        for elemento in range(0,9):
            for prox_elemento in range(elemento + 1, 9):
                if lista[elemento] != 0 and lista[prox_elemento] != 0:
                    if dict_ideal[lista[prox_elemento]] < dict_ideal[lista[elemento]]:
                            sum += 1
        return sum

    def FindEmpty(self):
        i = 0
        j = 0
        for linha in self.estado:
            for coluna in linha:
                if coluna == 0:
                    return i,j
                j+=1

            i+=1
            j=0
    
    def sucessors(self):

        
        sucessors = []
        i,j = self.FindEmpty()

        # if self.impossivel == True:
        #     sucessors.append(Eightpuzzle(self.estado,"up",i-1,j))
        #     return sucessors
        # i = self.i
        # j = self.j

        if (self.i-1 >= 0 and self.operator != "down"):
            alterado1 = copy.deepcopy(self.estado)
            alterado1[i][j] = alterado1[i-1][j] 
            alterado1[i-1][j] = 0
            # print("vou colocar o primeiro")
            # print(alterado1)
            sucessors.append(Eightpuzzle(alterado1,"up",i-1,j))
            
        if (i+1 <= 2 and self.operator != "up"):
            alterado2 = copy.deepcopy(self.estado)
            alterado2[i][j] = alterado2[i+1][j] 
            alterado2[i+1][j] = 0
            # print("vou colocar o segunda")
            # print(alterado2)
            sucessors.append(Eightpuzzle(alterado2,"down", i+1, j))
        if (j-1 >= 0 and self.operator != "right"):
            alterado3 = copy.deepcopy(self.estado)
            alterado3[i][j] = alterado3[i][j-1] 
            alterado3[i][j-1] = 0
            # print("aqui nao")
            sucessors.append(Eightpuzzle(alterado3, "left", i, j-1))
        if (j+1 <= 2 and self.operator != "leff"):
            alterado4 = copy.deepcopy(self.estado)
            alterado4[i][j] = alterado4[i][j+1]
            alterado4[i][j+1] = 0
            # print("vou colocar o terceiro")
            # print(alterado4)
            sucessors.append(Eightpuzzle(alterado4, "right", i, j+1))

        return sucessors
    
    def tilePenalty(self):
        objetivo = self.objetivo
        dict = {0:1,1:2,2:3,3:8,4:0,5:4,6:7,7:6,8:5}
        dict_invertido = {1:[0,0],2:[0,1],3:[0,2],4:[1,2],5:[2,2],6:[2,1],7:[2,0],8:[1,0],0:[1,1]}
        x = self.estado
        count = 0
        score2 = 0
        for i in x:
            for j in i:
                valor = j #numero que esta sendo analisado
                valor_certo = dict[count] # numero que deveria estar nessa posicao
                if valor != valor_certo and valor != 0:
                    casa_certa_i = dict_invertido[valor][0]
                    casa_certa_j = dict_invertido[valor][1]
                    valor_casa = x[casa_certa_i][casa_certa_j]
                    if valor_certo == valor_casa and valor_certo != 0:
                        score2 += 1
                count+=1
        return score2

    def is_goal(self):
        e = str(self.estado)
        o = str(self.objetivo)
        if e==o:
            return True
        else:
            return False
    
    def description(self):
        return "Problema do 8-puzzle"
    
    def cost(self):
        return 1

    def print(self):
        return (self.estado)

    def h(self):
        i = 1
        j = 1
        score = 0
        for linha in self.estado:
            for coluna in linha:
                if coluna != 0:
                    score += abs(i - self.correctPos[coluna][1]) + abs(j - self.correctPos[coluna][2])
                j+=1
            i+=1
            j=1
        return (score + self.tilePenalty())
        #return score
    
    def env(self):
        return str(self.estado)


def main():
    print('A estrela')
    matrix = np.array([[3,4,8],[1,2,5],[7,0,6]])
    state = Eightpuzzle(matrix,"",1,0)
    if(state.isSolvable()):
        algorithm = AEstrela()
        result = algorithm.search(state)
        if result != None:
            print('Achou!')
            print(result.show_path())
        else:
            print('Nao achou solucao')
    else:
        print("Impossivel")


if __name__ == '__main__':
    main()



