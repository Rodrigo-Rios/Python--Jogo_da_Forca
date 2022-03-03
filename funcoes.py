def ler_arquivo():

    # Lê arquivo de palavras.txt
    file = open("palavras.txt", "r")

    lista_palavras = []

    # Formata e joga as palavras para uma lista python
    for palavra in file:
        palavra = palavra.strip()
        palavra = palavra.casefold()
        lista_palavras.append(palavra)

    file.close()

    return lista_palavras
