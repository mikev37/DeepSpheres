'''
Merging---------------------------------------------

Create a new temp data structure

For every in 1st db character their All lines field is compared using word2vec to every character in the 2nd db
If they go beyond a certain similarity index, they are merged, and the new character is added to the new db

All lines are added with new 0m[index]m and add the new characters with a merged All lines and lines

Same is done with tokens, but now if the old line contained the old index, change the corresponding index position in the new db

Alternative to this solution is make the new indexes different from the old ones, for example 0t[index]t will not be confused with 0x[index]x
In this solution, we then use a regex and change the 0t[]t to 0x[]x so we can keep consistency for merging more than once and processing
This one might be better than the temp data structure idea, actually.

'''
import fuzzywuzzy.fuzz
import math
import DataStructures
from DataStructures import PlayData

def shouldMerge(corpusA,corpusB):
    try:
        count=0
        simTotal=0.0
        #Test each given and get the most similar given
        #Loop through all lines on the other corpus
        for lineA in corpusA:
            count=count+1
            simularity=0.0
            holdB="blank"
            for lineB in corpusB:
                tempComp=fuzzywuzzy.fuzz.WRatio(lineA[0].text,lineB[0].text)
                if simularity<tempComp:
                    simularity=tempComp
                    holdB=lineB
            #Test simularity of responses to the most similar givens
            simularity=1.0*simularity/100
            print lineA[0].text+"\n"+holdB[0].text+"\nGiven:"+str(simularity)
            temp=1.0*fuzzywuzzy.fuzz.WRatio(lineA[1].text,holdB[1].text)/100
            print lineA[1].text+"\n"+holdB[1].text+"\nResponse:"+str(temp)
            simTotal=simTotal+temp*simularity
        simularityA=simTotal/count*100/count
        print "Shouldmerge Debug:"+str(simularityA)
        return simularity>.5
    except AttributeError:
        return False
'''
chars to be merged
new list of characters
list of all line references
'''
def mergeChar(charA,charB,charListA,charListB,charListN):
    
    charN = DataStructures.CharacterObject(charA.name+charB.name)
    charN.anger = (charA.anger+charB.anger)/2
    charN.lines = charA.lines + charB.lines
    charListN.append(charN)
    indexN = charListN.index(charN)
    indexA = charListA.index(charA)
    indexB = charListB.index(charB)
    reIndex(indexA, indexN, charListA, charListN)
    reIndex(indexB, indexN, charListB, charListN)

    
    return charN

def mergeToken(charA,charB,tokenListA,tokenListB,tokenListN,charList):
    
    charN = DataStructures.TokenObject(charA.name+charB.name)
    charN.lines = charA.lines + charB.lines
    tokenListN.append(charN)
    indexN = tokenListN.index(charN)
    indexA = tokenListA.index(charA)
    indexB = tokenListB.index(charB)
    reIndexT(indexA, indexN, charList)
    reIndexT(indexB, indexN, charList)
    return charN

def reIndexT(indexA,indexN,charListN):
    for char in charListN:
        for line in char.lines:
            line[1].text = line[1].text.replace("0x"+str(indexA)+"x0","0t"+str(indexN)+"t0")  

def reIndex(indexA,indexN,charListA,charListN):
    for char in charListA:
        for line in char.lines:
            line[1].text = line[1].text.replace("0m"+str(indexA)+"m0","0z"+str(indexN)+"z0")
    for char in charListN:
        for line in char.lines:
            line[1].text = line[1].text.replace("0m"+str(indexA)+"m0","0z"+str(indexN)+"z0") 
            
def postProcess(playData):
    for char in playData.charList:
        print char.name
        for line in char.lines:
            if char.name == 'DIRECTION':
                print line[1].text
            line[1].text = postProcessLine(line[1].text)
    #for token in playData.tokenList:
    #    for line in token.lines:
    #        line[1].text = postProcessLine(line[1].text)       
             
def postProcessLine(line):
    line = line.replace("0t","0x")
    line = line.replace("t0","x0")
    line = line.replace("0z","0m")
    line = line.replace("z0","m0")
    print "POST PROCESSING LINE"+line
    print "____________________________________________"
    return line
    

def mergeDB(DBA,DBB):
    DBN = DataStructures.PlayData(DBA.playName+DBB.playName)
    
    print "TODO"
    unmergedCA = []
    unmergedTA = []
    unmergedCB = []
    unmergedTB = []
    for char in DBA.charList:
        unmergedCA.append(DBA.charList.index(char))
    for char in DBA.tokenList:
        unmergedTA.append(DBA.tokenList.index(char))
    for char in DBB.charList:
        unmergedCB.append(DBB.charList.index(char))
    for char in DBB.tokenList:
        unmergedTB.append(DBB.tokenList.index(char))
        
    for charA in DBA.charList:
        indexA = DBA.charList.index(charA)
        if indexA not in unmergedCA:
            continue
        for charB in DBB.charList:
            indexB = DBB.charList.index(charB)
            if(indexB not in unmergedCB):
                continue
            if(shouldMerge(charA.lines, charB.lines)):
                mergeChar(charA, charB, DBA.charList,DBB.charList, DBN.charList)
                if indexB in unmergedCB:
                    unmergedCB.remove(indexB)
                if indexA in unmergedCA:
                    unmergedCA.remove(indexA)
    #Go through each character A for each character B
    
    #Check if they're mergable
    
    #Get a character N for the characters merged
    
    for tokenA in DBA.tokenList:
        indexA = DBA.tokenList.index(tokenA)
        if indexA not in unmergedTA:
            continue
        for tokenB in DBB.tokenList:
            indexB = DBB.tokenList.index(tokenB)
            if indexB not in unmergedTB:
                continue           
            if(shouldMerge(charA.getAllLines(), charB.getAllLines())):
                mergeToken(tokenA, tokenB, DBA.tokenList, DBB.tokenList, DBN.tokenList, DBN.charList)
                unmergedTB.remove(indexB)
                unmergedTA.remove(indexA)
    
    
    
    #Add all the unmerged characters
    for indexA in unmergedCA:
        charA = DBA.charList[indexA]
        charN = DataStructures.CharacterObject(charA.name)
        charN.lines = charA.lines
        charN.anger = charA.anger
        DBN.charList.append(charN)
        indexN = DBN.charList.index(charN)
        reIndex(indexA, indexN, DBA.charList, DBN.charList)
    
    
    for indexB in unmergedCB:
        charB = DBB.charList[indexB]
        charN = DataStructures.CharacterObject(charB.name)
        charN.lines = charB.lines
        charN.anger = charB.anger
        DBN.charList.append(charN)
        indexN = DBN.charList.index(charN)
        reIndex(indexB, indexN, DBB.charList, DBN.charList)
        
        
        

    for indexA in unmergedTA:
        tokenA = DBA.tokenList[indexA]
        tokenN = DataStructures.TokenObject(tokenA.name)
        tokenN.lines = tokenA.lines
        DBN.tokenList.append(tokenN)
        indexN = DBN.tokenList.index(tokenN)
        reIndexT(indexA, indexN, DBN.charList)
    
    
    for indexB in unmergedTB:
        tokenB = DBB.tokenList[indexB]
        tokenN = DataStructures.TokenObject(tokenB.name)
        tokenN.lines = tokenB.lines
        DBN.tokenList.append(tokenN)
        indexN = DBN.tokenList.index(tokenN)
        reIndexT(indexB, indexN, DBN.charList)
    #Add all the scenes
    
    for scene in DBA.sceneList:
        DBN.sceneList.append(scene)
        
    for scene in DBB.sceneList:
        DBN.sceneList.append(scene)
    print DBN.charList
    DBN.meanLength = (DBA.meanLength+DBB.meanLength)/2
    DBN.meanStart = (DBA.meanStart+DBB.meanStart)/2
    DBN.numChars = (DBA.numChars+DBB.numChars)/2
    DBN.numLines = (DBA.numLines +DBB.numLines)/2
    DBN.numScenes = (DBA.numScenes +DBB.numScenes)/2
    DBN.charVar = math.sqrt(pow(DBA.numChars - DBB.numChars,2))
    #postProcess(DBA)
    #postProcess(DBB)
    postProcess(DBN)
    
    return DBN
    