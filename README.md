# JOGO DA FORCA


Projeto simples com o intuito de mostrar os conceitos de leitura de **arquivo**, **funções** e **estruturas de repetição** para os iniciantes de Python.


## Detalhes do jogo
---------------

O jogo possui um menu com as opções para jogar ou sair.

O jogo busca as palavras num o arquivo externo "words.txt" e transforma numa lista python.

O jogador pode acrescentar mais palavras no arquivo words.txt. 

Caso altere o nome ou o caminho do arquivo, terá que alterar no código também(read_words.py).

O jogo faz uma escolha dentro dessa lista de palavra, mascara e inicia o jogo.


## Regras:
---------------

* Número de jogadas é baseado no tamanho do palavra secreta mais 1.

* A cada letra informada o jogo verifica se a palavra já foi formada e o número de tentativas do jogador. 

* Caso a palavra seja formada, o jogo  encerra com o feedback positivo.<br>Caso o número de tentativas esgote, o jogo encerra com o feedback negativo 
