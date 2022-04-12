def ler_arquivo():

    # Lê arquivo de palavras.txt
    with open('palavras.txt','r') as file:
    	return list(palavra.strip().casefold() for palavra in file)
