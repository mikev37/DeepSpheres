'''
Creation---------------------------------------------------

A new Scene is created based on the average computed scene length + variation

scene length is taken as a function of scene length together with scene relation to current position through script

variation is the is the average squared deviation from the mean for scenes weighted by closeness to current position through script

    number of characters and number of character lines are created in a similar fashion
    Each character has a frustration meter which raises by the number of total lines he has
    The character with the highest frustration speaks
    Based on length of responce, the characters frustration and random chance the character's line might be extended, at which point he looks for a responce to his first line and concats it
    his frustration is then cleared
'''
import DataStructures
import random
from chatterbot import ChatBot

dirBot = ChatBot("Direction")

def createPlay(playdata):
    print "TODO"
    #get a cast of characters
    charbotsN = []
    charnum = playdata.meanChars+random.randint(playdata.charVariance)
    for i in range(0,charnum):
        j = random.randint(len(playdata.charList))
        if j not in charbotsN:
            charbotsN.append(j)
        else:
            i = i -1
def createScene(script,charbots):
    text = ""
    numChars = 0
    numLines = 0
    chars = []
    
    