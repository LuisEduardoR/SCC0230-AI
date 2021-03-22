# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794

import sys
import time
import labyrinth_base as lb

# Função de heuristica, a distância manhatan é usada
# pois no labirinto só se pode andar célula por célula
def manhattan_distance(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

# Função de hill climbing
def hill_climbing(labyrinth, start, end):

    # Guardam os tempos da função
    begin_time = None
    found_time = None

    # Guarda as dimensões do labirinto
    x = len(labyrinth)
    y = len(labyrinth[0])

    # Matriz que guarda os antecessores das posições já visitadas
    prev = [[[-1, -1] for i in range(y)] for j in range(x)]

    # Marca o elemento inicial para ser verificado primeiro
    cur = start
    
    # Marca a melhor heuristica encontrada até agora (inicia-se com um valor
    # maior que qualquer um que poderia ser retornado pela função)
    cur_dist = 2 * x * y

    # Marca o tempo de início e executa o hill climbing
    begin_time = time.time()
    while cur != None:

        # Verifica se um caminho foi encontrado
        # Se ele foi a busca encerra e o tempo é anotado
        if lb.is_end(labyrinth, cur):
            found = True
            found_time = time.time()
            break

        # Checa as adjacências do elemento e busca qual "colina subir"

        # Guarda o melhor elemento e seu valor na heuristica (inicia-se com um valor
        # maior que qualquer um que poderia ser retornado pela função)
        best = None

        # Direita
        next = lb.get_right(labyrinth, cur, prev) # [cur[0], cur[1] + 1]
        if next != None:
            # Escolhe esse nó se ele for melhor que o atual e melhor que os outros adjacentes (checado abaixo)
            next_dist = manhattan_distance(next, end)
            if next_dist < cur_dist:
                best = next 
                # Já atualiza a distância atual para usa-la nas checagens abaixo
                cur_dist = next_dist

        # Baixo
        next = lb.get_bottom(labyrinth, cur, prev) # [cur[0] + 1, cur[1]]
        if next != None:
            next_dist = manhattan_distance(next, end)
            if next_dist < cur_dist:
                best = next 
                cur_dist = next_dist

        # Esquerda
        next = lb.get_left(labyrinth, cur, prev) # [cur[0], cur[1] - 1]
        if next != None:
            next_dist = manhattan_distance(next, end)
            if next_dist < cur_dist:
                best = next 
                cur_dist = next_dist

        # Cima
        next = lb.get_top(labyrinth, cur, prev) # [cur[0] - 1, cur[1]]
        if next != None:
            next_dist = manhattan_distance(next, end)
            if next_dist < cur_dist:
                best = next 
                cur_dist = next_dist

        # "Sobe para a colina mais alta", se best for igual a None é porque o algoritmo
        # chegou em um melhor local, como não estamos usando backtracking ele deve parar
        if best != None:
            # Marca o antecessor do proximo elemento como sendo o atual
            prev[best[0]][best[1]] = [cur[0], cur[1]] 
            cur = best
        else:
            # Marca o tempo que o algoritmo finalizou
            found_time = time.time()
            break

    # Gera o caminho a partir da matriz de predecessores
    # Nota-se que passamos cur ao invés de end para a função,
    # Isso é feito para podermos checar o melhor local encontrado
    # pelo algoritmo, já que muitas vezes ele não é capaz de achar
    # o melhor global
    path = lb.prev_to_path(prev, start, cur)

    # Retorna um objeto com os resultados
    return lb.Result(path, found_time - begin_time)          

if __name__ == '__main__':
    
    # Chama a execução padrão do algoritmo
    lb.execute_algorithm(hill_climbing)