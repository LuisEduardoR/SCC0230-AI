# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794
#
# Esse programa foi criado para receber entradas de labirintos e strings contendo saídas esperadas
# e convert~e-las para imagens de visualização mais fácil.
#
# Para utiliza-lo são necessários os módulos imageio e numpy
# Caso você tenha o pip instalado eles podem ser obtidos executando o comando:
#
#   ´pip install imageio numpy´
#
# Uso:
# - Execute esse script passando um arquivo contendo uma entrada de um labirinto
# - O programa tentará carregar o labirinto e depois solicitará a entrada de um texto,
#   esse texto deve conter o caminho esperado de um certo algoritmo para esse labirinto
# - Sobre o caminho:
#   - Garante que o caminho seja realmente válido, erros serão mostrados caso esse caminho
#     ultrapasse obstáculos (-) no labirinto ou acesse posições fora dele
# - Sobre a saída:
#   - A imagem gerada como saída segue as especificações definidas em "conversor_labirintos.py"
#     com a adição de que posições presentes no caminho são marcadas com verde (RGB: 0, 255, 0)

import sys
import imageio
import numpy as np

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

# Converte a string do labirinto para uma imagem
def str_to_img(labyrinth):

    # Cria a imagem vazia inicialmente
    img = np.zeros((len(labyrinth), len(labyrinth[0]), 3))

    # Passa pelos elementos do labirinto e os converte para a cor equivalente
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
        
            # Detecta um espaço livre
            if labyrinth[x][y] == '*':
                img[x][y] = [255, 255, 255]

            # Detecta um obstáculo
            elif labyrinth[x][y] == '-':
                img[x][y] = [0, 0, 0]

            # Detecta o início
            elif labyrinth[x][y] == '#':
                img[x][y] = [0, 0, 255]

            # Detecta o fim
            elif labyrinth[x][y] == '$':
                img[x][y] = [255, 0, 0]

            # Detecta caractéres inválidos
            else:
                print('ERRO: A entrada contém um caractér inválido! (Pos: [{},{}])'.format(x, y))
                exit(1)

    return img

def add_path(img, path_str):

    # Guarda o caminho
    path = []

    # Lê a string e encontra os elementos do caminho
    # Remove os colchetes ao redor da entrada
    path_str = path_str[1:-1]
    # Substitui alguns caractéres para simplificar os delimitadores
    path_str = path_str.replace(',(', '').replace('(', '').replace(')', ';')
    # Separa os elementos
    path_str = path_str.split(';')

    # Converte os elementos do formato string para o formato usado no caminho
    for elem in path_str:

        # Ignora a string vazia que é deixada em path_str
        if elem == '':
            continue

        # Separa as duas coordenadas do elemento
        pos_str = elem.split(',')

        # Converte as coordenadas para int e as adiciona ao caminho
        path.append([int(pos_str[0]), int(pos_str[1])])

    # Agora que temos o caminho colorimos de verde seus elementos na imagem
    for pos in path:

        # Detecta uma posição do caminho fora do labirinto
        if pos[0] > img.shape[0] or pos[1] > img.shape[1] or pos[0] < 0 or pos[1] < 0:
            print('ERRO: Um dos elementos do caminho está fora do labirinto!')
            exit(1)

        # Obtém a cor original da posição no caminho
        cur = img[pos[0]][pos[1]]

        # Verifica que esse caminho não está sobre um obstáculo
        if cur[0] == 0 and cur[1] == 0 and cur[2] == 0:
            print('ERRO: Um dos elementos do caminho está sobre um obstáculo!')
            exit(1)

        # Colore apenas se o pixel nessa posição é branco (preserva a cor original do início e do fim)
        if cur[0] == 255 and cur[1] == 255 and cur[2] == 255:
            img[pos[0]][pos[1]] = [0, 255, 0]


# Função principal
def main():

    # Detecta se o número de argumentos está correto
    if len(sys.argv) != 2:
        print('ERRO: Número incorreto de argumentos! Uso: <nome desse arquivo>.py <nome da entrada>' )
        exit(1)

    # Tenta carregar o arquivo de entrada
    labyrinth = load_labyrinth(sys.argv[1])

    # Converte o labirinto para uma imagem
    img = str_to_img(labyrinth)

    # Recebe o caminho
    print('Entrada carregada com sucesso! Insira agora o caminho:')
    path_str = input()

    # Adiciona o caminho sobre a imagem
    add_path(img, path_str)

    # Salva a imagem
    imageio.imwrite('caminho.bmp', img.astype(np.uint8))

    print('Conversão bem sucedida!')

if __name__ == '__main__':
    main()
    

