import math
from wordgen import gen_word
def postProcess(line):
    line.replace("0t","0x")
    line.replace("t0","x0")
    line.replace("0z","0m")
    line.replace("z0","m0")
    

def computeVariance(scenes):
    meanStart = 0
    meanLength = 0
    for scene in scenes:
        meanStart = meanStart + scene.start
        meanLength = meanLength + scene.length
        
    meanStart = meanStart/len(scenes)
    meanLength = meanLength/len(scenes)
    
    for scene in scenes:
        scene.vLength = math.sqrt(pow(meanLength-scene.length,2))
        scene.vStart = math.sqrt(pow(meanLength-scene.length,2))
     

def replaceTokens(line,characters,tokens):
    
    for char in characters:
        line.replace("0m"+characters.index(char)+"0m",characters.newName)
    for token in characters:
        line.replace("0x"+tokens.index(char)+"0x",tokens.newName)
    
    
    