# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794

import sys
import time
import labyrinth_base as lb

# Função de busca em profundidade
def dfs(labyrinth, start, end):
    
    # Guardam os tempos da função
    begin_time = None
    found_time = None

    # Stack usada para a DFS
    stack = [start]

    # Guarda as dimensões do labirinto
    x = len(labyrinth)
    y = len(labyrinth[0])

    # Matriz que guarda os antecessores das posições já visitadas
    prev = [[[-1, -1] for i in range(y)] for j in range(x)]

    # Marca se um caminho foi encontrado
    found = False

    # Marca o tempo de início e executa a DFS
    begin_time = time.time()
    while len(stack) != 0:

        # Remove o primeiro elemento da pilha
        cur = stack.pop()

        # Verifica se um caminho foi encontrado
        # Se ele foi a busca encerra e o tempo é anotado
        if lb.is_end(labyrinth, cur):
            found = True
            found_time = time.time()
            break

        # Checa as adjacências do elemento e as coloca na pilha se não foram visitadas

        # Direita
        next = lb.get_right(labyrinth, cur, prev) # [cur[0], cur[1] + 1]
        if next != None:
            stack.append(next) # Adiciona na pilha
            prev[next[0]][next[1]] = cur # Marca o antecessor do proximo elemento como sendo o atual

        # Baixo
        next = lb.get_bottom(labyrinth, cur, prev) # [cur[0] + 1, cur[1]]
        if next != None:
            stack.append(next)
            prev[next[0]][next[1]] = cur

        # Esquerda
        next = lb.get_left(labyrinth, cur, prev) # [cur[0], cur[1] - 1]
        if next != None:
            stack.append(next)
            prev[next[0]][next[1]] = cur

        # Cima
        next = lb.get_top(labyrinth, cur, prev) # [cur[0] - 1, cur[1]]
        if next != None:
            stack.append(next)
            prev[next[0]][next[1]] = cur

    # Gera o caminho a partir da matriz de predecessores
    path = lb.prev_to_path(prev, start, end)

    # Retorna um objeto com os resultados
    if found:
        return lb.Result(path, found_time - begin_time)
    return lb.Result(None, None)

if __name__ == '__main__':
    
    # Chama a execução padrão do algoritmo
    lb.execute_algorithm(dfs)