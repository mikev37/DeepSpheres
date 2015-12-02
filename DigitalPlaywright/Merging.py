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

import DataStructures

def shouldMerge(corpusA,corpusB):
    #TODO
    return False
'''
chars to be merged
new list of characters
list of all line references
'''
def mergeChar(charA,charB,charListA,charListB,charListN):
    
    charN = DataStructures.CharacterObject(charA.name+charB.name)
    charListN.append(charN)
    indexN = charListN.index(charN)
    indexA = charListA.index(charA)
    indexB = charListB.index(charB)
    for char in charListA:
        for line in char.lines:
            line.replace("0m"+indexA+"m0","0t"+indexN+"t0")
    for char in charListB:
        for line in char.lines:
            line.replace("0m"+indexB+"m0","0t"+indexN+"t0")
    charN.lines = charA.lines + charB.lines
    
    return charN

def mergeToken(charA,charB,charListA,charListB,charListN):
    
    charN = DataStructures.CharacterObject(charA.name+charB.name)
    charListN.append(charN)
    indexN = charListN.index(charN)
    indexA = charListA.index(charA)
    indexB = charListB.index(charB)
    for char in charListA:
        for line in char.lines:
            line.replace("0x"+indexA+"x0","0z"+indexN+"z0")
    for char in charListB:
        for line in char.lines:
            line.replace("0x"+indexB+"x0","0z"+indexN+"z0")
    charN.lines = charA.lines + charB.lines

    return charN

    
def postProcess(line):
    line.replace("0t","0x")
    line.replace("t0","x0")
    line.replace("0z","0m")
    line.replace("z0","m0")
    
    

def mergeDB(DBA,DBB):
    DBN = DataStructures.PlayData()
    
    print "TODO"
    unmergedCA = []
    unmergedTA = []
    unmergedCB = []
    unmergedTB = []
    #Go through each character A for each character B
    
    #Check if they're mergable
    
    #Get a character N for the characters merged
    
    #Add all the unmerged characters
    
    #Add all the scenes
    
    #Recompute statistics
    
    