from read_words import open_file
import random

"""Pega uma palavra aleatória da lista e depois transforma numa palavra secreta"""
def create_secret_word():
    
    list_words = open_file()
    secret_word = []
    random_word = random.choice(list_words)
    secret_word = ["_" for _ in range(len(random_word))]

    return random_word, secret_word