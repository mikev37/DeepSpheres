import math
from wordgen import gen_word
def postProcess(line):
    line.replace("0t","0x")
    line.replace("t0","x0")
    line.replace("0z","0m")
    line.replace("z0","m0")
    

'''
given list of characternames and list of tokennames, replace all the temp data with new data
'''
def replaceTokens(line,characters,tokens):
    
    for char in characters:
        line.replace("0m"+characters.index(char)+"0m",char)
    for token in characters:
        line.replace("0x"+tokens.index(token)+"0x",token)
    
    
    