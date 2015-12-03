import json
import os
import string
from ArchetypeGen import split_into_sentences

def SaveCorpusi(playData):
    os.mkdir("./"+playData.playName)
    os.chdir("./"+playData.playName)
    for char in playData.charList:
        name = char.name.replace(".","")
        name = name.replace("/","")
        name = filter(lambda x: x in string.printable,name)
        os.mkdir("./"+name)
        saveName = str(name)+'.json'
        os.chdir("./"+name)
        openFile = open(saveName, 'w')
        openFile.write("{ \"lines\" :  \n") 
        print char.name
        data = []
        for line in char.lines:
            print line[0].text
            print line[1].text
            dataLine =[line[0].text]
            dataLine = dataLine + split_into_sentences(line[1].text)
            data.append(dataLine)
        json.dump(data, openFile, indent=3)
        openFile.write("\n }")
        openFile.close()
        os.chdir("..")
    return