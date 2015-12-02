import math
from wordgen import gen_word

def replaceTokens(line,characters,tokens):
    
    for char in characters:
        line.replace("0m"+characters.index(char)+"0m",characters.newName)
    for token in characters:
        line.replace("0x"+tokens.index(char)+"0x",tokens.newName)
    
    
    