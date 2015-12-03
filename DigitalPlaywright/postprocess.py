import math
from wordgen import gen_word
def postProcess(line):
    line = line.replace("0t","0x")
    line = line.replace("t0","x0")
    line = line.replace("0z","0m")
    line = line.replace("z0","m0")
    return line

'''
given list of characternames and list of tokennames, replace all the temp data with new data
'''
def replaceTokensLine(line,characters,tokens):
    
    for char in characters:
        line = line.replace("0m"+str(characters.index(char))+"m0",char)
    for token in tokens:
        line = line.replace("0x"+str(tokens.index(token))+"x0",token)
    return line
    
def replaceTokens(playData,script):
    charList = []
    tokenList = []
    
    
    for i in range(0,len(playData.charList)+5):
        charList.append(gen_word(2, 4))
        
    for i in range(0,len(playData.tokenList)+5):
        tokenList.append(gen_word(2, 4))
    print "_________________"
    print charList
    print tokenList
    print ""
    print ""
    print ""    
    return replaceTokensLine(script,charList,tokenList)
    