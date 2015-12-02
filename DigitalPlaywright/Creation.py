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
import math
from chatterbot import ChatBot



def createPlay(playdata):
    print "TODO"
    #get a cast of characters
    dirBot = ChatBot("Direction")
    charbotsN = []
    charnum = playdata.meanChars+random.randint(playdata.charVariance)
    for i in range(0,charnum):
        j = random.randint(len(playdata.charList))
        if j not in charbotsN:
            charbotsN.append(j)
        else:
            i = i -1
    charBots = [] 
    for j in charbotsN:
        charBots.append(playdata.charList[j])
    pos = 0
    script = ""
    while (pos < 1):
        scene = createScene(script, charBots, pos, dirBot)
        script = script + scene['text'] + "\n"
        pos = pos + scene['scene'].length
        
    script = script + "\n\n\t\t\t END"
    
    return script
        
def createScene(playdata,charBots, pos, dirBot):
    text = ""
    line = ""
    numChars = 0
    numLines = 0
    dirFrustration = 0
    dirAnger = 0
    chars = []
    scene = DataStructures.SceneObject()
    for part in playdata.sceneList:
        scene.length = scene.length + (part.length + random.random()*part.vLength)*part.getContribution(pos)
        numChars = numChars + math.ceil(len(part.characters)*part.getContribution(pos))
        dirAnger = math.ceil(len(part.characters)*part.getContribution(pos))
    scene.length = scene.length/len(playdata.sceneList)
    numLines = playdata.meanLines*scene.length
    for i in range(0,numChars):
        chars.append(charBots[random.randint(len(charBots))])
    while numLines > 0:
        numLines = numLines - 1
        talk = chars[0]
        for temp in chars:
            if temp.frustration > talk.frustration :
                talk = temp
            temp.frustration = temp.frustration + temp.anger
        if talk.frustration > dirFrustration:
            text = text + "\t\t 0m"+str(talk.index)+"m0\n"
            line = talk.getResponce(line)
            text = text + "\t"+line+"\n"
            talk.frustration = 0
            dirFrustration = dirFrustration+dirAnger
        else : 
            line = dirBot.get_response(line)
            text = text + line  + "\n"
            dirFrustration = 0
        
    return {'text':text, 'scene': scene }
    