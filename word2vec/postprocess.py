import math
from wordgen import gen_word
def postProcess(line):
    line.replace("0t","0x")
    line.replace("t0","x0")
    
    
class Scene:
    
    def __init__(self):
        self.start = 0
        self.length = 0
        self.vLength = 0
        self.vStart = 0
        self.characters = []
        self.directions = []
        self.name = ""
    #
    def getContribution(self,pos):
        return abs(pos - self.start+self.length/2)
    
    
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
    
    
    