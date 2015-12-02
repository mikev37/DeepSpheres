


import json
import re

saveName = 'data.json'

class PlayData:
    def __init__(self, name):
        self.playName = name
        self.charList = []
        self.tokenList = []
        self.sceneList = []
        self.numChars = 0
        self.numScenes = 0
        self.numLines = 0
        
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
    
masterLineList = []

def GetLines():
    global masterLineList
    global saveName
    with open(saveName, 'r') as data_file:
        data = json.load(data_file)
    for lineObject in data["lines"]:
        masterLineList.append(lineObject)



class CharActor():
    name = ""
    lines = []
    def __init__ (self, name):
        self.name = name.strip()

listCharActors = []

def isInCharList(name):
    for actor in listCharActors:
        if actor.name == name:
            return True
        else:
            return False
        
#Section for intelligently splitting a string into seperate sentances
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def makeLineObj(JSONLine):
    temp = LineObj(JSONLine['scriptName'],
                   JSONLine['sceneNum'],
                   JSONLine['lineNum'],
                   JSONLine['characterName'],
                   JSONLine['lineText'])
    return temp

PlayList = []
scriptWatcher = ""
lineCounter = 0
sceneCounter = -1
charWatcher = []

def resetCounters():
    global lineCounter
    global sceneCounter
    global charWatcher
    lineCounter = 0
    sceneCounter = -1
    charWatcher = []
    return

def UpdatePreviousScene():
    global PlayList
    global scriptWatcher
    global lineCounter
    global sceneCounter
    global charWatcher
    temp = next(play for play in PlayList if play.playName == scriptWatcher)
    temp.sceneList[sceneCounter].numChars = charWatcher.count()
    charWatcher = []
    temp.sceneList[sceneCounter].length = lineCounter
    lineCounter = 0
    return
    
def UpdatePreviousScript():
    global PlayList
    global scriptWatcher
    global lineCounter
    global sceneCounter
    global charWatcher
    temp = next(play for play in PlayList if play.playName == scriptWatcher)
    temp.numScenes = temp.sceneList.count()
    
def AddToStructures(line):
    global PlayList
    global scriptWatcher
    global lineCounter
    global sceneCounter
    global charWatcher
    #if new play
    if line.script != scriptWatcher:
        UpdatePreviousScene()
        scriptWatcher = line.script
        resetCounters()
        PlayList.append(PlayData(line.script))
    lineCounter += 1
    #if new Scene
    if line.scene != sceneCounter:
        UpdatePreviousScene()
        sceneCounter = line.scene
        temp = SceneObject()
        temp.start = lineCounter
        temp.name = line.scene + " - " + sceneCounter
        next(play for play in PlayList if play.playName == scriptWatcher).sceneList.append(temp)
    #if new Character
    if line.character not in charWatcher:
        charWatcher.append(line.character)
    return
        
def UpdateValuesInPlays(): 
    global PlayList
    for play in PlayList:
        charNum = 0
        for scene in play.
    

def CombineInChars():
    global masterLineList
    global listCharActors
    previousLine = None      #to keep lines in pairs, call and response
    for line in masterLineList:
        print "checking Line"
        found = False
        for actor in listCharActors:
            if actor.name == line['characterName']:         #Find the character in the char list
                found = True
                actor.lines.append([previousLine, line])
        if not found:
            listCharActors.append(CharActor(line['characterName']))
            for actor in listCharActors:
                if actor.name == line['characterName']:         #Find the character in the char list
                    found = True
                    actor.lines.append([previousLine, line])
        AddToStructures(line)
        previousLine = line
            
            
            

GetLines()
CombineInChars()
for guy in listCharActors:
    print "Character: " + guy.name
    #for said in guy.lines:
        #for what in said:
            #print "    -" + what
    
print "done"


