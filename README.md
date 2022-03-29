# 8_puzzle

### Descricao do problema
Durante esse exercicio foi desenvolvido um agente autonomo para resolver o problema do 8 puzzle.

### Estados
Os estados sao representados por um np array em 2d de formato 3x3


### Gerecao de sucessores
O primeiro passo eh achar onde esta a posicao vazia. Feito isso o algoritmo calcula quais sao os passos possiveis para aquela situacao, dentre eles (cima, baixo, direita, esquerda) - considerando que o movimento e a da casa vazia.

### Heuristicas utilizadas
[^1]: Distancia de Manhatam - Soma da distancia entre a posicao atual e a posicao objetivo (tanto no eixo x quanto no y) de todos os valores, 0 nao incluso.
[^2]: Tile Penality - Se houver um par de valores trocados ha um "custo" de um para cada valor.