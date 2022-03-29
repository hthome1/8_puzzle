from SearchAlgorithms import AEstrela
from Eightpuzzle import Eightpuzzle
from datetime import date, datetime
import numpy as np

def test_1():
    matrix = np.array([[8,1,3],[0,7,2],[6,5,4]])
    print("testando isso: ", matrix)
    state = Eightpuzzle(matrix,"op",1,0)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    objetivo = str(np.array([[1,2,3],[8,0,4],[7,6,5]]))
    assert result.state.env() == objetivo

def test_2():
    matrix = np.array([[7,8,6],[2,3,5],[0,1,4]])
    print("testando isso: ", matrix)
    state = Eightpuzzle(matrix,"op",2,0)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    objetivo = str(np.array([[1,2,3],[8,0,4],[7,6,5]]))
    assert result.state.env() == objetivo

def test_3():
    matrix = np.array([[7,8,6],[2,3,5],[1,4,0]])
    print("testando isso: ", matrix)
    state = Eightpuzzle(matrix,"op",2,2)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    objetivo = str(np.array([[1,2,3],[8,0,4],[7,6,5]]))
    assert result.state.env() == objetivo

def test_4():
    matrix = np.array([[8,3,6],[7,5,4],[2,1,0]])
    print("testando isso: ", matrix)
    state = Eightpuzzle(matrix,"op",2,1)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    objetivo = str(np.array([[1,2,3],[8,0,4],[7,6,5]]))
    assert result.state.env() == objetivo
