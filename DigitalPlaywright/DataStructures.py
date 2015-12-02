from wordgen import gen_word




class PlayData:
    def __init__(self):
        self.charList = []
        self.tokenList = []
        self.sceneList = []
        #reference to every line]
        self.lineList = []

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
            words = words + line.text
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


class SceneObject:
    
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