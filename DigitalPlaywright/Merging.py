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
def mergeChar(charA,charB,charListA,charListB,charListN,lineList):
    
    charN = DataStructures.CharacterObject()
    
    charN.lines = charA.lines + charB.lines
    
    for line in lineList:
        line.replace("0m"+"m0")
    #TODO
    
def mergeDB(DBA,DBB):
    print "TODO"
    