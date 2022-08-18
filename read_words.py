import unicodedata

""" Retira os acentos das letras"""
def remove_accent(word):
    
    word  = unicodedata.normalize('NFD', word)
    word  = word.encode('ascii', 'ignore')
    word  = word.decode('utf_8')
    return word


""" Lê as palavras do arquivo e cria uma lista"""
def open_file():
   
    with open("words.txt","r") as file:
        words = [remove_accent(word).strip().casefold() for word in file]
    
    return words