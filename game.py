from funcoes import ler_arquivo
import random
import os

os.system("cls")

# Pega o retorno a função ler_arquivo e armazena na varáivel lista
lista = ler_arquivo()

# Pega um número aleatório baseado no tamanho da lista de palavras
numb = random.randint(0, len(lista))

# Pega uma palavra com o número aleatório e armazena na palavra aleatória
palavra_aleatoria = str(lista[numb]).casefold()
palavra_secreta = []

# print(palavra_aleatoria)

# Transforma a palavra aletória em palavra secreta com "_" ocupando o index de acordo com o tamanho da palavra aleatória
for letra in range(len(palavra_aleatoria)):
    palavra_secreta.append("_")

print(palavra_secreta)

contador = 1
for i in range(len(palavra_aleatoria)):

    letra = input("Digite uma letra:")
    letra = letra.casefold()

    if letra in palavra_aleatoria:
        for i in range(len(palavra_aleatoria)):
            if letra == palavra_aleatoria[i]:
                palavra_secreta[i] = letra
        # Verifica se a palavra já foi preenchida
        if "_" not in palavra_secreta:

            print("\n", palavra_secreta)
            print("Parabéns você acertou a palavra secreta!")
            break

    # Verifica se chegamos ao final das tentivas e a palavra não foi preenchida
    if contador == len(palavra_secreta):
        print("\nNão acertou a palavra secreta!!!")
        print(f"A palavra secreta era: {palavra_aleatoria}")
        break
    contador += 1

    print(palavra_secreta)
