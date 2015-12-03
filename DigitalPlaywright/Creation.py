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
import string
from chatterbot import ChatBot
import os
def makeBot(playName,name):
    pame = name.replace(".","")
    pame = pame.replace("/","")
    pame = filter(lambda x: x in string.printable,pame)
    bot = ChatBot(pame)
    bot.gg()
    bot = ChatBot(pame)
    print playName+'.'+pame
    print os.getcwd()
    bot.train(playName+'.'+pame)
    return bot

def createPlay(playdata):
    print "TODO"
    #get a cast of characters
    charbotsN = []
    print playdata.numChars
    print playdata.charVars
    charnum = playdata.numChars+random.randint(0,playdata.charVars/2)
    print "Cast "+str(charnum)
    
    for i in range(0,charnum):
        j = random.randint(0,len(playdata.charList)-1)
        if j not in charbotsN:
            charbotsN.append(j)
        else:
            i = i -1
    print charbotsN
    charBots = [] 
    characters = []
    indexi = {}
    for j in charbotsN:
        charBots.append(makeBot(playdata.playName, playdata.charList[j].name))
        characters.append(playdata.charList[j])
    pos = 0
    script = ""
    #make scenes until done
    while (pos < 1):
        scene = createScene(playdata, characters, pos, charBots,playdata.charList)
        script = script + scene['text'] + "\n"
        pos = pos + scene['scene'].length
        
    script = script + "\n\n\t\t\t END"
    
    return script
        
def createScene(playdata,characters, pos, castBots,charList):
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
        numChars = math.floor(numChars + part.numChars*part.getContribution(pos))
        #dirAnger = math.ceil(len(part.characters)*part.getContribution(pos))
        
    scene.length = scene.length/len(playdata.sceneList)
    scene.length = max(scene.length,.1)
    numChars = max([numChars,3])
    numLines = playdata.numLines*scene.length
    chatBots = []
    print scene.length
    print numChars
    for i in range(2,int(numChars)):
        j = random.randint(0,len(characters)-1)
        chars.append(characters[j])
        chatBots.append(castBots[j])
        
    if len(chars) < 2:
        j = random.randint(0,len(characters)-1)
        chars.append(characters[j])
        chatBots.append(castBots[j])
        j = random.randint(0,len(characters)-1)
        chars.append(characters[j])
        chatBots.append(castBots[j])
    while numLines > 0:
        numLines = numLines - 1
        talk = chars[0]
        for temp in chars:
            if temp.frustration > talk.frustration :
                talk = temp
            temp.frustration = temp.frustration + temp.anger
        print talk.name
        print chars.index(talk)
        print chatBots
        print chars
        bot = chatBots[chars.index(talk)]
        
        if 'DIRECTION' in talk.name:
            line = bot.get_response(line)
            text = text +line+"\n"
            talk.frustration = 0
        else:
            text = text + "\t\t 0m"+str(charList.index(talk))+"m0\n"
            line = bot.get_response(line)
            text = text + "\t"+line+"\n"
            talk.frustration = 0

        
        
    return {'text':text, 'scene': scene }
    