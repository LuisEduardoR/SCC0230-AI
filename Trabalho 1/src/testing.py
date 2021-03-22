# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794

import os
import time

import labyrinth_base as lb
import dfs as alg_dfs
import bfs as alg_bfs
import best_first_search as alg_best_first
import a_star as alg_a_star
import hill_climbing as alg_hill_climbing

class PathResult:
    def __init__(self, path):
        self.path = path

class TimeResult:
    def __init__(self, time_to_find):
        if time_to_find != None:
            self.times_to_find = [time_to_find]
        else:
            self.times_to_find = None

# Preencha com o número de algoritmos aqui.
num_algorithms = 5

# Faz a execução dos testes para o algoritmo passado em alg e escreve
# os resultados em path_results e time_results. Um indíce único entre
# 0 e num_algorithms deve ser passado para cada algoritmo, ele será
# usado para salvar os resultados na linha certa das matrizes de resultado.
# labyrinths são os labirintos em que os testes devem ser executados e num_times 
# é o número de vezes que o teste deve ser executado para medir o tempo
def execute_test(index, alg, path_results, time_results, labyrinths, num_times):

    # Faz a primeira execução pegando o tempo e o caminho
    for l in range(len(labyrinths)):

        # Encontra o inicio e o fim do labirinto
        start = lb.find_start(labyrinths[l])
        end = lb.find_end(labyrinths[l])

        # Encontra o caminho
        result = alg(labyrinths[l], start, end)

        # Salva o resultados nas matrizes
        path_results[index][l] = PathResult(result.path)
        if result.time_to_find != None:
            time_results[index][l] = TimeResult(result.time_to_find)
        else:
            time_results[index][l] = TimeResult(None)

    # Faz as demais execuções pegando apenas o tempo
    for _i in range(1, num_times):
        for l in range(len(labyrinths)):

            # Encontra o inicio e o fim do labirinto
            start = lb.find_start(labyrinths[l])
            end = lb.find_end(labyrinths[l])

            # Encontra o caminho
            result = alg(labyrinths[l], start, end)

            # Adiciona os tempos na matriz de resultados
            if result.time_to_find != None:
                time_results[index][l].times_to_find.append(result.time_to_find)

# Faz a conversão dos resultados para um texto no formato correto de saída
# os resultados são passados em path_results e time_results. output é a string
# a ser modificada. Um indíce único entre 0 e num_algorithms deve ser passado 
# em index para cada algoritmo, ele será usado para identifica os quais são os 
# resultados de cada algoritmo.
def add_results(index, path_results, time_results):

    # Coloque aqui os nomes dos algoritimos a serem usados no output ordenados por indice
    algorithm_names = ['dfs', 'bfs', 'best_first_search', 'a_star', 'hill_climbing']

    # Escreve o nome do algoritmo na saida
    output = algorithm_names[index] + ' {\n'

    # Escreve para cada labirinto:
    output += '\tlabyrinths {\n'
    for l in range(len(path_results[index])):
        output += '\t\t' + str(l + 1) + ' {\n'

        output += '\t\t\tpath {\n'

        # Converts the path into a string.
        path_str = lb.path_to_string(path_results[index][l].path)
        if path_str != None:
            output += '\t\t\t\t' + path_str + '\n'
        else:
            output += '\t\t\t\tNone\n'

        output += '\t\t\t},\n'

        if time_results[index][l].times_to_find != None:
            output += '\t\t\ttime: \"' + str(average(time_results[index][l].times_to_find)) + '\"\n'
        else:
           output += '\t\t\ttime: failed\"\n'

        output += '\t\t}\n'
    output += '\t}\n'

    # Finaliza a escrita desse algoritmo
    output += '},\n'

    return output

# Função básica de média aritmética
def average(values):
    sum = 0
    for val in values:
        sum += val
    return val / len(values)

def main():

    # Recebe o número de vezes que cada algoritmo será executado
    # para tirar-se a média dos tempos de execução
    print('Entre o número de testes para cada algoritmo: ')
    try:
        num_tests = int(input())
        if num_tests < 1:
            raise ValueError('number must be a positive integer other than 0')
    except Exception as error:
        print('Entrada inválida! ({})'.format(error))
        exit(1)

    # Checa se exite uma pasta ./testes
    print('Procurando por pasta \"./testes\"...')
    if not os.path.isdir('./testes'):
        print('O diretório \"./testes\" não foi encontrado!')
        print('É necessário criar um diretório \"./testes\" junto deste arquivo!')
        exit(1)

    # Procura por arquivos de teste na pasta
    print('Procurando por arquivos de teste em \"./testes\"...')
    test_files = [f for f in os.listdir('./testes') if os.path.isfile(os.path.join('./testes', f))]
    
    # Checa se existem arquivos no diretório
    if len(test_files) < 1:
        print("Nenhum arquivo encontrado em \"./testes\"!")
        exit(1)
    print("{} arquivos encontrados!".format(len(test_files)))

    # Carrega os labirintos
    labyrinths = []
    for file in test_files:
        try:
            print("Carregando {}...".format(file))
            labyrinths.append(lb.load_labyrinth(os.path.join('./testes', file)))
        except:
            print("Falha ao carregar {}! Ignorando...".format(file))
    
    # Checa quantos testes foram carregados com sucesso
    if len(labyrinths) < 1:
        print("Todos os testes falharam em carregar!")
        exit(1)
    print("{} de {} testes carregados com sucesso!".format(len(test_files), len(test_files)))

    # Executa os testes para cada algoritmo
    print("Executando...")

    # Guarda os caminhos retornados pelos testes, para economizar memória, como os resultados para um mesmo 
    # labirinto sempre são iguais, pega o resultado sempre da primeira execução
    path_results = [[None for i in range(len(labyrinths))] for j in range(num_algorithms)]

    # Guarda os tempos retornados pelos testes
    time_results = [[None for i in range(len(labyrinths))] for j in range(num_algorithms)]

    # Marca o tempo de início
    t_begin = time.time()

    # Executa os testes para cada algoritmo:
    # DFS
    print('> DFS...')
    execute_test(0, alg_dfs.dfs, path_results, time_results, labyrinths, num_tests)
    # BFS
    print('> BFS...')
    execute_test(1, alg_bfs.bfs, path_results, time_results, labyrinths, num_tests)
    # Best-First-Search
    print('> Best-First-Search...')
    execute_test(2, alg_best_first.best_first_search, path_results, time_results, labyrinths, num_tests)
    # A*
    print('> A*...')
    execute_test(3, alg_a_star.a_star, path_results, time_results, labyrinths, num_tests)
    # Hill Climbing
    print('> Hill Climbing...')
    execute_test(4, alg_hill_climbing.hill_climbing, path_results, time_results, labyrinths, num_tests)

    # Marca o tempo de final
    t_end = time.time()

    print('Execução finalizada com sucesso! ({} labirintos; {} testes cada; para {} algoritmos)'.format(len(labyrinths), num_tests, num_algorithms))
    print('Tempo total de execução: %.1fs' % (t_end - t_begin))

    # Salva os resultados em um arquivo output.txt
    print("Salvando resultados...")

    # Cria uma string com o contéudo a ser escrito para output
    output_txt = ''
    
    # Adiciona os dados de cada algoritmos no output
    for a in range(num_algorithms):
        output_txt += add_results(a, path_results, time_results)

    # Escreve a string de output para um arquivo
    try:
        with open('./output.txt', 'w') as text_file:
            text_file.write(output_txt)
    except:
        print('Não foi possível escrever o arquivo de saída!')
        exit(1)
    
    print('Resultados salvos com sucesso para \"output.txt\"!')

if __name__ == '__main__':
    main()