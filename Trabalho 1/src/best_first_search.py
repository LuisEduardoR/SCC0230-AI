# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794

import sys
import time
import labyrinth_base as lb

# Guarda o valor do final de maneira acessível a função de ordenação
global_end = [-1, -1]

# Função de ordenção para a fila de prioridades, a distância manhatan é usada
# pois no labirinto só se pode andar célula por célula
def manhattan_distance(elem):
    return abs(elem[0] - global_end[0]) + abs(elem[1] - global_end[1])

# Função de best-first search
def best_first_search(labyrinth, start, end):
    
    # Marca o final do labirinto de forma que seja acessível à função de ordenação
    global global_end
    global_end = end

    # Guardam os tempos da função
    begin_time = None
    found_time = None

    # Priority queue usada para a best-first search
    p_queue = [start]

    # Guarda as dimensões do labirinto
    x = len(labyrinth)
    y = len(labyrinth[0])

    # Matriz que guarda os antecessores das posições já visitadas
    prev = [[[-1, -1] for i in range(y)] for j in range(x)]

    # Marca se um caminho foi encontrado
    found = False

    # Marca o tempo de início e executa a best-first search
    begin_time = time.time()
    while len(p_queue) != 0:

        # Ordena a fila baseada em uma heuristica
        p_queue.sort(key=manhattan_distance)

        # Remove o primeiro elemento da fila
        cur = p_queue.pop(0)

        # Verifica se um caminho foi encontrado
        # Se ele foi a busca encerra e o tempo é anotado
        if lb.is_end(labyrinth, cur):
            found = True
            found_time = time.time()
            break

        # Checa as adjacências do elemento e as coloca na priority queue se não foram visitadas

        # Direita
        next = lb.get_right(labyrinth, cur, prev) # [cur[0], cur[1] + 1]
        if next != None:
            p_queue.append(next) # Adiciona na fila
            prev[next[0]][next[1]] = cur # Marca o antecessor do proximo elemento como sendo o atual

        # Baixo
        next = lb.get_bottom(labyrinth, cur, prev) # [cur[0] + 1, cur[1]]
        if next != None:
            p_queue.append(next)
            prev[next[0]][next[1]] = cur

        # Esquerda
        next = lb.get_left(labyrinth, cur, prev) # [cur[0], cur[1] - 1]
        if next != None and prev[next[0]][next[1]] == [-1, -1]:
            p_queue.append(next)
            prev[next[0]][next[1]] = cur

        # Cima
        next = lb.get_top(labyrinth, cur, prev) # [cur[0] - 1, cur[1]]
        if next != None and prev[next[0]][next[1]] == [-1, -1]:
            p_queue.append(next)
            prev[next[0]][next[1]] = cur

    # Gera o caminho a partir da matriz de predecessores
    path = lb.prev_to_path(prev, start, end)

    # Retorna um objeto com os resultados
    if found:
        return lb.Result(path, found_time - begin_time)
    return lb.Result(None, None)

if __name__ == '__main__':
    
    # Chama a execução padrão do algoritmo
    lb.execute_algorithm(best_first_search)