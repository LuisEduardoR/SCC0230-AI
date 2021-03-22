# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794

import sys

# Esse script contém as funções básicas que são usadas pelas outras implementações.

# Objeto que contém o retorno dos resultados de um algoritmo
class Result:
    def __init__(self, path, time_to_find):
        self.path = path
        self.time_to_find = time_to_find

# Cria uma array contendo ao labirinto a partir do nome de um arquivo a ser aberto
def load_labyrinth(name):
    
    # Lê o arquivo para uma string
    try:
        with open(name, 'r') as text_file:
            txt = text_file.read()
    except:
        print('ERRO: Não foi possível abrir o arquivo de texto!')
        exit(1)

    # Quebra o arquivo em linhas
    lines = txt.splitlines()

    # Obtém as dimensões do labirinto e cria a array
    dim = [int(s) for s in lines[0].split() if s.isdigit()]
    labyrinth = [[None for x in range(dim[1])] for y in range(dim[0])] 

    # Copia informação das linhas do arquivo de texto para o labirinto.
    for x in range(0, dim[0]):
        for y in range(0, dim[1]):
            labyrinth[x][y] = lines[x+1][y]

    return labyrinth

# Retorna a posição do ínicio do labirinto.
def find_start(labyrinth):
    for x in range(0, len(labyrinth)):
        for y in range(0, len(labyrinth[x])):
            if is_start(labyrinth, [x, y]):
                return [x, y]

# Retorna a posição do final do labirinto.
def find_end(labyrinth):
    for x in range(0, len(labyrinth)):
        for y in range(0, len(labyrinth[x])):
            if is_end(labyrinth,[x, y]):
                return [x, y]

# Retorna se a posição é um obstáculo
def is_obstacle(labyrinth, pos):

    if labyrinth[pos[0]][pos[1]] == '-':
        return True

    return False

# Retorna se a posição é o início do jogo
def is_start(labyrinth, pos):

    if labyrinth[pos[0]][pos[1]] == '#':
        return True

    return False

# Retorna se a posição é o final do jogo
def is_end(labyrinth, pos):

    if labyrinth[pos[0]][pos[1]] == '$':
        return True

    return False

# Retorna a posição da direita da posição passada ou None se não houver, for um obstáculo ou já tiver sido visitada
def get_right(labyrinth, pos, prev):
    
    # Pega as dimensões do labirinto
    # x = len(labyrinth)
    y = len(labyrinth[0])

    # Pega a posição da direita e verifica se ela é válida e não é um obstáculo
    next = [pos[0], pos[1] + 1]
    if next[1] < y:
        if not is_obstacle(labyrinth, next) and prev[next[0]][next[1]] == [-1, -1]:
            return next

    # Se a posição não for válida retorna None
    return None

# Retorna a posição da esquerda da posição passada ou None se não houver, for um obstáculo ou já tiver sido visitada
def get_left(labyrinth, pos, prev):
    
    # Pega as dimensões do labirinto
    # x = len(labyrinth)
    # y = len(labyrinth[0])

    # Pega a posição da esquerda e verifica se ela é válida e não é um obstáculo
    next = [pos[0], pos[1] - 1]
    if next[1] >= 0:
        if not is_obstacle(labyrinth, next) and prev[next[0]][next[1]] == [-1, -1]:
            return next

    # Se a posição não for válida retorna None
    return None

# Retorna a posição de baixo da posição passada ou None se não houver, for um obstáculo ou já tiver sido visitada
def get_bottom(labyrinth, pos, prev):
    
    # Pega as dimensões do labirinto
    x = len(labyrinth)
    # y = len(labyrinth[0])

    # Pega a posição de baixo e verifica se ela é válida e não é um obstáculo
    next = [pos[0] + 1, pos[1]]
    if next[0] < x:
        if not is_obstacle(labyrinth, next) and prev[next[0]][next[1]] == [-1, -1]:
            return next

    # Se a posição não for válida retorna None
    return None

# Retorna a posição de cima da posição passada ou None se não houver, for um obstáculo ou já tiver sido visitada
def get_top(labyrinth, pos, prev):
    
    # Pega as dimensões do labirinto
    # x = len(labyrinth)
    # y = len(labyrinth[0])

    # Pega a posição de cima e verifica se ela é válida e não é um obstáculo
    next = [pos[0] - 1, pos[1]]
    if next[0] >= 0:
        if not is_obstacle(labyrinth, next) and prev[next[0]][next[1]] == [-1, -1]:
            return next

    # Se a posição não for válida retorna None
    return None

# Converte um caminho para string
def path_to_string(path):

    # Retorna None se o caminho não existe
    if path == None:
        return None

    # Faz a conversão
    output = '['
    path_len = len(path)
    for i in range(path_len):
        if i != 0:
            output += ','
        output += '({},{})'.format(path[i][0], path[i][1])
    output += ']'
    return output

# Imprime o caminho ou uma mensagem caso ele seja None
def print_path(path):

    # Transforma o caminho em uma string no formato correto
    path_str = path_to_string(path)

    # Faz a impressão
    if path_str == None:
        print("Nenhum caminho encontrado!")
    else:
        print(path_str)

# Faz a impressão dos tempos relevantes para as buscas
def print_times(begin, found, end):

    print("Tempos:")
    if found != None:
        print("> Primeiro caminho encontrado: %.8fs" % (found - begin))
    else:
        print("> Primeiro caminho encontrado: não encontrado")
    print("> Fim da execução: %.8fs" % (end - begin))

# Converte a matriz de predecessores gerada por um algoritmo de busca em um caminho
def prev_to_path(prev, start, end):

    # Se um caminho foi encontrado, podemos reconstruir o caminho na 
    # ordem inversa a partir dos predecessores
    reversed_path = []

    # Detecta se o caminho não pode ser encontrado
    if prev[end[0]][end[1]] == [-1, -1]:
        return None

    # Inicia no final do caminho e volta pelos antecessores até chegar no início
    cur = end
    while cur != start:
        reversed_path.append(cur)
        cur = prev[cur[0]][cur[1]]

    # Adiciona o início no final do caminho
    reversed_path.append(start)

    # Inverte o caminho encontrado acima para o formato correto e o retorna
    path = []
    path_len = len(reversed_path)
    for i in range(path_len):
        path.append(reversed_path[path_len - 1 - i])
    return path

# Inicia o processo de execução de um algoritmo, recebendo o nome de um arquivo contendo um labirinto como argumento
# e fazendo a impressão dos resultados
def execute_algorithm(alg):

    # Detecta se o número de argumentos está correto
    if len(sys.argv) != 2:
        print('ERRO: Número incorreto de argumentos! Uso: <nome desse arquivo>.py <nome do arquivo de texto>' )
        exit(1)

    # Carrega o labirinto do arquivo fornecido
    labyrinth = load_labyrinth(sys.argv[1])

    # Encontra o inicio e o fim do labirinto
    start = find_start(labyrinth)
    end = find_end(labyrinth)

    # Encontra o caminho
    result = alg(labyrinth, start, end)
    
    # Imprime a saída
    print_path(result.path)

    # Imprime os tempos
    # print_times(result.begin_time, result.found_time, result.end_time)