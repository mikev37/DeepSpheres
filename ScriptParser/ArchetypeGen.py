


import json
import re

saveName = 'data.json'

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
    

def CombineInChars():
    global masterLineList
    global listCharActors
    previousLine = ""       #to keep lines in pairs, call and response
    for line in masterLineList:
        print "checking Line"
        found = False
        for actor in listCharActors:
            if actor.name == line['characterName']:         #Find the character in the char list
                found = True
                actor.lines.append([previousLine] + split_into_sentences(line['lineText']))
        if not found:
            listCharActors.append(CharActor(line['characterName']))
            
        previousLine = line['lineText']
            
            
            

GetLines()
CombineInChars()
for guy in listCharActors:
    print "Character: " + guy.name
    #for said in guy.lines:
        #for what in said:
            #print "    -" + what
    
print "done"


