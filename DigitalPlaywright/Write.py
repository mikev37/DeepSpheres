import DataStructures
from Creation import createPlay
from Merging import mergeDB
from postprocess import replaceTokens
from PreProcess import tokenize
from PreProcess import computeVariance
from PreProcess import reToken
from Corpus import SaveCorpusi
from wordgen import gen_word
from ArchetypeGen import GetTheStuff
'''
lineO = DataStructures.LineObj("Hamlet",0,0,"DIRECTION","Hamlet")
lineA = DataStructures.LineObj("Hamlet",0,0,"DIRECTION","It was a sunny day")
lineB = DataStructures.LineObj("Hamlet",0,1,"JACKAL","Hello")
lineC = DataStructures.LineObj("Hamlet",0,2,"TERRY","Hi")
lineD = DataStructures.LineObj("Hamlet",0,3,"DIRECTION","It started raining, the 0x0x0 was wet")
lineE = DataStructures.LineObj("Hamlet",0,4,"TERRY","What wonderful weather, 0m2m0")
lineF = DataStructures.LineObj("Hamlet",0,5,"JACKAL","I can't believe it")
lineG = DataStructures.LineObj("Hamlet",0,6,"DIRECTION","0m1m0 draws his sword")
lineAA = [lineO,lineA]
lineAB = [lineA,lineB]
lineBC = [lineB,lineC]
lineCD = [lineC,lineD]
lineDE = [lineD,lineE]
lineEF = [lineE,lineF]
lineFG = [lineF,lineG]
charA = DataStructures.CharacterObject("DIRECTION")
charB = DataStructures.CharacterObject("JACKAL")
charC = DataStructures.CharacterObject("TERRY")

charA.anger = .2
charB.anger = .2
charC.anger = .2

charC.lines = [lineBC,lineDE]
charB.lines = [lineAB,lineEF]
charA.lines = [lineAA,lineCD,lineFG]

sceneA = DataStructures.SceneObject()
sceneA.numChars = 3
sceneA.length = 1
sceneA.start = 0

scriptA = DataStructures.PlayData("HAMLET")
scriptA.charList = [charA,charB,charC]
scriptA.numChars = 3
scriptA.numLines = 7
scriptA.numScenes = 1
scriptA.sceneList = [sceneA]
scriptA.tokenList = []



##############################################################3
lineO1 = DataStructures.LineObj("Hamlet",0,0,"DIRECTION","IHamlet")
lineA1 = DataStructures.LineObj("Hamlet",0,0,"DIRECTION","It was a sunny day")
lineB1 = DataStructures.LineObj("Hamlet",0,1,"JACKAL","Hello")
lineC1 = DataStructures.LineObj("Hamlet",0,2,"TERRY","Hi")
lineD1 = DataStructures.LineObj("Hamlet",0,3,"DIRECTION","It started raining, the 0x0x0 was wet")
lineE1 = DataStructures.LineObj("Hamlet",0,4,"TERRY","What wonderful weather, 0m2m0")
lineF1 = DataStructures.LineObj("Hamlet",0,5,"JACKAL","I can't believe it")
lineG1 = DataStructures.LineObj("Hamlet",0,6,"DIRECTION","0m1m0 draws his sword")
lineAA1 = [lineO1,lineA1]
lineAB1 = [lineA1,lineB1]
lineBC1 = [lineB1,lineC1]
lineCD1 = [lineC1,lineD1]
lineDE1 = [lineD1,lineE1]
lineEF1 = [lineE1,lineF1]
lineFG1 = [lineF1,lineG1]
charA1 = DataStructures.CharacterObject("DIRECTION")
charB1 = DataStructures.CharacterObject("JACKAL")
charC1 = DataStructures.CharacterObject("TERRY")

charA1.anger = .2
charB1.anger = .2
charC1.anger = .2

charC1.lines = [lineBC1,lineDE1]
charB1.lines = [lineAB1,lineEF1]
charA1.lines = [lineAA1,lineCD1,lineFG1]

sceneB = DataStructures.SceneObject()
sceneB.numChars = 3
sceneB.length = 1
sceneB.start = 0

scriptB = DataStructures.PlayData("HAMLET")
scriptB.charList = [charA1,charB1,charC1]
scriptB.numChars = 3
scriptB.numLines = 7
scriptB.numScenes = 1
scriptB.sceneList = [sceneB]
scriptB.tokenList = []
######################################################################################


'''
#Pull charcters and scenes from all the Line
scriptA = GetTheStuff()[0]
scriptB = GetTheStuff()[1]
#tokenize the play and compute statistics


tokenList = []
nameList = []
for char in scriptA.charList:
    nameList.append(char.name)
for char in scriptA.charList:
    for line in char.lines:
        print line[1].text
        line[1].text = tokenize(line[1].text, tokenList, nameList)
        print line[1].text
        

print scriptA

tokenList = []
nameList = []
for char in scriptB.charList:
    nameList.append(char.name)
for char in scriptB.charList:
    for line in char.lines:
        print line[1].text
        line[1].text = tokenize(line[1].text, tokenList, nameList)
        print line[1].text\
     

computeVariance(scriptA)   
reToken(tokenList,scriptA)
reToken(tokenList,scriptB)   
computeVariance(scriptB)

print scriptB

#merge play datas until there's only one

scriptN = mergeDB(scriptA, scriptB)

print ""
print "-After merge"
print ""
for char in scriptN.charList:
    print char.name
    for line in char.lines:
        print "\t"+line[1].text
print scriptN

#create corpusi from PlayData
#SaveCorpusi(scriptN)

#create play
nameList = []
tokenList = []
for char in scriptN.charList:
    nameList.append(gen_word(2,4))
for token in scriptN.tokenList:    
    tokenList.append(gen_word(1, 5))
    


script = createPlay(scriptN)

print replaceTokens(scriptN,script)
