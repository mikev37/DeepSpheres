from wordgen import gen_word

import math


class PlayData:
    def __init__(self, name):
        self.playName = name
        self.charList = []
        self.tokenList = []
        self.sceneList = []
        self.numChars = 0
        self.numScenes = 0
        self.numLines = 0
        self.meanStart = 0
        self.meanLength = 0
        self.charVars = 0
        
class SceneObject:
    
    def __init__(self):
        self.start = 0
        self.length = 0
        self.vLength = 0
        self.vStart = 0
        self.numChars = 0
        self.directions = []
        self.name = ""
    #
    def getContribution(self,pos):
        return 1.1-math.sqrt(math.pow(pos - (self.start),2))
    

class LineObj():
    script = ""
    scene = 0
    line = 0
    character = ""
    text = ""
    def __init__ (self, name, sc, ln, ch, txt):
        self.script = name.strip()
        self.scene = sc
        self.line = ln
        self.character = ch.strip()
        self.text = txt
    
class CharacterObject:
    
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.frustration = 0
        self.anger = 0 #number of lines/
        
    
    def generateName(self):
        self.name = gen_word(1,4)
        
    def getAllLines(self):
        words = ""
        for line in self.lines:
            words = words + line[1].text
        return words

class TokenObject:
    
    def __init__(self, name):
        self.name = name
        self.lines = []
    
    def generateName(self):
        self.name = gen_word(1,4)
        
    def getAllLines(self):
        words = ""
        for line in self.lines:
            words = words + line.text
        return words


