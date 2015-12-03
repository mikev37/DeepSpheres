'''
PreProcessing------------------------------------------

All names saved in an object
    Name : String
    All lines : String
    Lines : [Line]
    
Array of names contains all these objects

Each time a name is found in the line text, their name is replaced by 0m[index in name array]m

Tokens are essentially treated as names
    Token : String
    All lines : String
    Lines : [Line]

After processing for all the names, all the proper nouns are replaced by 0x[index of proper noun in array]x

Line object 
    name : CharObject
    Call : String
    Responce : String

All Scene headings get saved in an object

SceneObj
    Length of Scene as proportion of Play 0 to 1
    Start of scene as porportion of Play 0 to 1
    names contained
    Tokens contained
    
'''
import string
import DataStructures
from nltk.tag import pos_tag
from nltk.corpus import cmudict
from wordgen import gen_word
import re
import math
'''
takes in a line 
give it a list of all character names and all tokens already known
replaces all name names with 0m[]m
replaces all tokens with 0x[]x
'''
def tokenize(sentence,tokenList,nameList):
    
    tagged_sent = pos_tag(sentence.split())
    
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    print propernouns
    
    for noun in propernouns:
        poun = noun.translate(string.maketrans("",""), string.punctuation)
        if poun.upper() in nameList:
            sentence = sentence.replace(noun, "0m"+str(nameList.index(noun.upper()))+"m0")
        elif percentageUpper(noun) or "\'" in noun > .5 :
            continue
        else :
            if noun not in tokenList:
                tokenList.append(noun)
            sentence = sentence.replace(noun, "0x"+str(tokenList.index(noun))+"x0")

    return sentence

def percentageUpper(text):
    s = ''.join([c for c in text if c.isupper()])
    return 1.0*len(s)/len(text)

def reToken(tokenList,scriptA):
    for toke in tokenList:
        token = DataStructures.TokenObject(toke)
        for char in scriptA.charList:
            for line in char.lines:
                print "rt \r"
                if "0x"+str(tokenList.index(toke))+"x0" in line:
                    token.lines.append(line)
                    
        scriptA.tokenList.append(token)  

'''
Compute statistics needed for scene generation
'''
def computeVariance(playdata):
    scenes = playdata.sceneList
    meanStart = 0
    meanLength = 0
    for scene in scenes:
        meanStart = meanStart + scene.start
        meanLength = meanLength + scene.length
        
    meanStart = meanStart/len(scenes)
    meanLength = meanLength/len(scenes)
    playdata.meanStart = meanStart
    playdata.meanLength = meanLength
    playdata.numLines = playdata.numLines/2
    for scene in scenes:
        scene.vLength = math.sqrt(pow(meanLength-scene.length,2))
        scene.vStart = math.sqrt(pow(meanLength-scene.length,2))
     