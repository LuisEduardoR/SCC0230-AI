Para executar os códigos é necessário o **Python** (aconselha-se o uso do Python 3 em uma versão recente)

---

**Caso algum dos arquivos .py contendo os algoritmos seja movido para outra pasta, garanta que uma cópia do arquivo `labyrinth_base.py` seja movida junto, esse arquivo contém muitas funções básicas que são compartilhadas entre os algoritmos e é necessário para sua execução.**

---

Os arquivos a seguir contém os respectivos algoritmos:

- `dfs.py`:                 Busca em Profundidade
- `bfs.py`:                 Busca em Largura
- `best_first_search.py`:   Busca Best-First-Search
- `a_star.py`:              Busca A*
- `hill_climbing.py`:       Hill Climbing

Para executar qualquer algoritmo, abra um terminal e navegue até a pasta contendo o código em um terminal e execute o comando:

    python <nome do arquivo> <caminho para um arquivo contendo a entrada>

A pasta `testes` nesse diretório contém alguns arquivos de entrada com labirintos que podem ser usados. Para isso substitua:

    <caminho para um arquivo contendo a entrada>

Por:

    ./testes/<nome do arquivo de teste>

Também é fornecido o arquivo `testing.py`, ao executa-lo pelo comando:

    python testing.py

Será pedido o número de vezes que se deseja executar cada algoritmo em cada labirinto, em seguida ele buscará automaticamente na pasta `testes` por arquivos de teste válidos e executará todos os algoritmos várias vezes para cada caso de teste escrevendo os caminhos encontrados e as médias dos tempos de cada algoritmo para cada labirinto no arquivo `output.txt`. A formatação do arquivo `output.txt` se assemelha a um `.json`, nota-se que os números que identificam os labirintos são dados em ordem alfabética, ou seja o arquivo de teste que aparece primeiro na ordem alfabética será identificado como **1**.

---

Esse diretório também contém a pasta `extras`, nela temos o arquivo `conversor_labirintos.py` que permite converter imagens `.bmp` seguindo algumas especificações em arquivos `.txt` que podem ser usados como entrada. Além disso, também há as imagens que geraram os arquivos na pasta `testes`. Mais informações estão disponíveis em um comentário no início do arquivo .py dentro dela.

Dentro desse mesmo diretório também temos o arquivo `conversor_caminhos.py` que permite passar um arquivo de entrada e uma string contendo a saída de um algoritmo, ele gerará
uma imagem `caminho.bmp` contendo o labirinto que orginou aquela entrada com o caminho passado marcado nela. Mais informações estão disponíveis em um comentário no início do arquivo .py dentro dela.