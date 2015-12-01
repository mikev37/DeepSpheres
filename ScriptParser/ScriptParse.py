'''
Created on Nov 2, 2015

@author: karl
'''
#!/usr/bin/python
#import _mysql

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import json
from os import walk, remove
from collections import namedtuple
#from ccm.Pages import Page
#from libxml2 import lineNumbersDefault

sourceLoc = "sources/"
saveName = 'data.json'

def GetFileList():
    fileList = []
    for (dirpath, dirnames, filenames) in walk(sourceLoc):
        fileList.extend(filenames)
        break
    return fileList
    
   
scriptName = ""  #initialize to name of file for each script run     
lineNum = 0   #initialize to 1 plus largest line_id in database
sceneNum = 0   #initialize to 1 plus largest scene_id in database
characterName = ""   #set during parse, but can add new characters on the fly, using char_id
isLine = False

def ResetGlobals():
    global scriptName
    global lineNum
    global sceneNum
    global characterName
    global isLine   
    scriptName = "" 
    lineNum = 0
    sceneNum = 0
    characterName = ""
    isLine = False    
    return
    

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
    
masterList = []   

def LineAdd(script, scene, line, characterName, text): 
    global lineNum
    lineNum = lineNum + 1
    temp = LineObj(script, scene, lineNum, characterName, text)
    masterList.append(temp)
    return

def SaveAll():
    global masterList
    global saveName
    for line in masterList:
        data ={
               'scriptName'     :   line.script,
               'sceneNum'       :   line.scene,
               'lineNum'        :   line.line,
               'characterName'  :   line.character,
               'lineText'       :   line.text
               }
        with open(saveName, 'a') as openFile:
            json.dump(data, openFile, indent=3)
    return


#SORTERS
def checkScene(text, indent):
    return indent>100 and indent<120

def checkSceneHeading(text,indent):
    return percentageUpper(text) > .8

def checkCharacter(text, indent):
    return removeParentesis(text).isupper() and indent>200 and indent<300

#UTILITY
def percentageUpper(text):
    s = ''.join([c for c in text if c.isupper()])
    return 1.0*len(s)/len(text)

def percentageNumbers(text):
    s = ''.join([c for c in text.strip()[0:-2] if c.isdigit()])
    return 1.0*len(s)/len(text)

def removeParentesis(text):
    text = text+" "
    if len(text[text.rfind(")"):]) > 1 :
        return (text[0:text.find("(")]+text[text.rfind(")")+1:]).strip()
    else:
        return (text[0:text.find("(")]).strip()
    

def ParseLine(text, indent):
    global scriptName
    global lineNum
    global sceneNum
    global characterName
    global isLine

    #kill switch
    if "cid:13" in text:
        return
    if percentageNumbers(text) > .3:
        return
    if "CONTINUED" in text:
        return
    if(len(removeParentesis(text).strip())==0):
        return
    text = text.replace('\n', '')
    
    #Scene start
    if (checkScene(text, indent)):
        firstBit = text[:5]
        if (checkSceneHeading(text, indent)):
            #is a new scene, add to database
            print "\n Scene: " + text
            sceneNum = sceneNum + 1
        else:
            #Otherwise it must be directions
            lineNum = lineNum + 1
            LineAdd(scriptName, sceneNum, lineNum, "DIRECTION", removeParentesis(text))
        
    #Character name
    elif (checkCharacter(text, indent)):
        #is a Character name, check if it's in the database with appropriate script & get new char_id
        isLine=True
        characterName = removeParentesis(text)

    
    #Actual line, always immediately after a character name
    elif (isLine):
        isLine = False
        #add line to database with char_id = characterNum, line num and scene num each 
        lineNum = lineNum + 1
        LineAdd(scriptName, sceneNum, lineNum, characterName, removeParentesis(text))

        
    return

TextBlock = namedtuple("TextBlock",["x","y","text"])

def GetScript(filename):
    global scriptName
    ResetGlobals()
    scriptName = filename
    password = ""
    # Open a PDF file.
    fp = open(filename, 'rb')
    # Create a PDF parser object associated with the file object.
    parser = PDFParser(fp)
    # Create a PDF document object that stores the document structure.
    # Supply the password for initialization.
    document = PDFDocument(parser, password)
    # Check if the document allows text extraction. If not, abort.
    if not document.is_extractable:
        print "---Not translatable---"
        return
        #raise PDFTextExtractionNotAllowed
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    device = PDFDevice(rsrcmgr)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
    
    # Set parameters for analysis.
    laparams = LAParams()
    laparams.boxes_flow = 2
    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for pgnum,page in enumerate(PDFPage.create_pages(document)):
        if pgnum == 0:
            continue
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        text = []
        for page in layout:
            try:
                if page.get_text().strip():
                    text.append(TextBlock(page.x0,page.y1,page.get_text().strip()))
            except:
                temp=5  
            print ".",
        text.sort(key = lambda row:(-row.y))
        # Parse all of the "line" objects in each page
        for line in text:
            ParseLine(line.text, line.x)


# ---BEGIN PROCEDURAL SEQUENCE---

fileList = GetFileList()
open(saveName, 'w')  #clear old file for creation of new
for fileName in fileList:
    print "\n" + fileName
    GetScript(sourceLoc + fileName)
    
SaveAll()
    
