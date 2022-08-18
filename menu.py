from game import game
import os
import time

"""Menu do jogo da forca"""
def menu():

    print("=" * 15 + " Bem vindo ao jogo da forca " + "=" * 15 )
    print("\n")
    print("=" * 20 + " Menu " + "=" * 20)
    print("1 - Jogar")
    print("2 - Sair")

    option = input("Digite a opção desejada:")

    if option == "1":
        game()
        print("\nRetornando para o menu...")
        time.sleep(3) 
        os.system("cls" if os.name == "nt" else "clear")
        menu()
    elif option == "2":
        exit()
    else:
        print("Opção inválida. Retornando para o menu...")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        menu()