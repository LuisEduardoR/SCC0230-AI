# Aline Fernanda da Conceição 9437275
# Letícia Lima Aledi 11274942
# Luís Eduardo Rozante de Freitas Pereira 10734794
#
# Esse programa foi criado para converter imagens .bmp para arquivos .txt contendo a entrada
# especificada para o trabalho.
#
# Para utiliza-lo são necessários os módulos imageio e numpy
# Caso você tenha o pip instalado eles podem ser obtidos executando o comando:
#
#   ´pip install imageio numpy´
#
# Uso:
# - Execute esse script passando uma imagem em formato bitmap (.bmp)
# - Sobre a imagem:
#   - O formato bitmap é usado pois não tem compressão
#   - Pixels pretos (RGB: 0, 0, 0) se tornaram obstáculos (-)
#   - Pixels brancos (RGB: 255, 255, 255) se tornaram espaços livres (*)
#   - Deve haver um único pixel azul (RGB: 0, 0, 255) que se tornará o início (#)
#   - Deve haver um único pixel vermelho (RGB: 255, 0, 0) que se tornará o fim ($)

import sys
import imageio

# Abre a imagem
def open_img(name):
    return imageio.imread(name)

# Converte a imagem para uma cadeia de caracteres
def img_to_str(img):

    # Usadas para checar que há apenas um início e um fim
    found_srt = False
    found_end = False

    # Usada para contruir a string que será retornada, inica-se a string com as dimensões da imagem
    ret = '{} {}\n'.format(img.shape[0], img.shape[1])

    # Passa pelos pixels da imagem e os converte para seu carácter equivalente
    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
        
            # Detecta um pixel branco
            if img[x, y, 0] == 255 and img[x, y, 1] == 255 and img[x, y, 2] == 255:
                ret += '*'

            # Detecta um pixel preto
            elif img[x, y, 0] == 0 and img[x, y, 1] == 0 and img[x, y, 2] == 0:
                ret += '-'

            # Detecta um pixel azul
            elif img[x, y, 0] == 0 and img[x, y, 1] == 0 and img[x, y, 2] == 255:
                if not found_srt:
                    ret += '#'
                    found_end = True
                else:
                    print('ERRO: A imagem contém mais de um início! (Pixel: [{},{}])'.format(x, y))
                    exit(1)

            # Detecta um pixel vermelho
            elif img[x, y, 0] == 255 and img[x, y, 1] == 0 and img[x, y, 2] == 0:
                if not found_srt:
                    ret += '$'
                    found_srt = True
                else:
                    print('ERRO: A imagem contém mais de um fim! (Pixel: [{},{}])'.format(x, y))
                    exit(1)

            # Detecta pixels de cores inválidas
            else:
                print('ERRO: A imagem contém um pixel inválido! (Pixel: [{},{}])'.format(x, y))
                exit(1)

        ret += '\n'

    # Detecta que há um início definido na imagem.
    if not found_srt:
        print('ERRO: A imagem não contém um início! (RGB: 0, 0, 255)')
        exit(1)
    
    # Detecta que há um fim definido na imagem.
    if not found_end:
        print('ERRO: A imagem não contém um fim! (RGB: 255, 0, 0)')
        exit(1)

    return ret

# Salva a cadeia de caracteres para um arquivo .txt
def save_str(s, name):
    
    try:
        with open(name, 'w') as text_file:
            text_file.write(s)
    except:
        print('ERRO: Não foi possível criar o arquivo de texto!')
        exit(1)

# Função principal
def main():

    # Detecta se o número de argumentos está correto
    if len(sys.argv) != 2:
        print('ERRO: Número incorreto de argumentos! Uso: <nome desse arquivo>.py <nome da imagem>.bmp' )
        exit(1)

    # Checa que a imagem está no formato bitmap
    img_name = sys.argv[1]
    img_name_split = img_name.split('.')
    img_format = img_name_split[len(img_name_split) - 1]
    if img_format != 'bmp':
        print('ERRO: A imagem deve estar no formato bitmap (.bmp)! Formato atual: {}'.format(img_format))
        exit(1)

    # Tenta abrir a imagem passada como argumento
    try:
        img = open_img(img_name)
    except:
        print('ERRO: Não foi possível abrir a imagem!')
        exit(1)

    # Converte a imagem para o formato de texto
    string_img = img_to_str(img)

    # Cria o nome para o arquivo de texto
    txt_name = img_name[0:len(img_name) - 4] + '.txt'

    # Salva a imagem
    save_str(string_img, txt_name)

    print('Conversão bem sucedida!')

if __name__ == '__main__':
    main()
    

