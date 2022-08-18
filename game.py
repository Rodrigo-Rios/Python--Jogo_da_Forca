from create_secret_word import create_secret_word

"""Inicia o jogo e faz as verificações a cada tentativa.
   Analisa se a palavra secreta foi preenchida
   Verifica se o número de tentativas esgotou 
"""
def game():
    """ Armazena a palavra aleatória e secreta gerada pela função create_secret_word a cada novo game"""
    random_word, secret_word = create_secret_word()

    print(secret_word)
    attempts = 1

    for i in range(len(random_word) + 1):

        char = input("Digite uma letra:").casefold()

        index = [index for index, item in enumerate(random_word) if item == char]
        
        for i in index:
            secret_word[i] = char

        if "_" not in secret_word:
            print(f"\nPalavra secreta: {random_word} \nParabéns você acertou")
            break
    
        if attempts == len(secret_word) + 1:
            print(f"\nNão acertou a palavra secreta! Palavra secreta: {random_word}")
            break
        
        attempts += 1

        print(secret_word)