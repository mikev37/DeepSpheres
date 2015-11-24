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
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator
import time
from collections import namedtuple
#from ccm.Pages import Page
#from libxml2 import lineNumbersDefault



  
def GetDatabase():
    dbPassword = "into0myheart"
    dbUser = "karl"
    dbHost = "localhost"
    dbName = "Plays"
    #db=_mysql.connect(host=dbHost,user=dbUser,
    #              passwd=dbPassword,db=dbName)
    #if not db:
    #    print "didn't connect"
          
lineNum = 0   #initialize to 1 plus largest line_id in database
sceneNum = 0   #initialize to 1 plus largest scene_id in database
characterNum = 0   #set during parse, but can add new characters on the fly, using char_id
isLine = False

charName = "" #Temporary storage of character names
charTemp = {} #Temporary storage of character lines
charName = ""
sceneTemp = [] #Temporary storage of scenes
class Scene():
    name = ""
    phrases = {}
    chars = []
    dirs = []
    tokens = []
    def __init__ (self,name):
        self.name = name.strip()
        self.chars = []
        self.phrases = {}
        self.dirs = []
        self.tokens = []

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
    
    global lineNum
    global sceneNum
    global sceneTemp
    global sceneName
    global charName
    global charTemp
    global characterNum
    global isLine

    #kill switch
    if "cid:13" in text:
        return
    if percentageNumbers(text) > .3:
        return
    if "CONTINUED" in text:
        return
    if(len(text.strip())==0):
        return
    
    print ""
    print text.strip(),indent
    print ""
    
    #Scene start
    if (checkScene(text, indent)):
        print "scene" + text
        firstBit = text[:5]
        if (checkSceneHeading(text, indent)):
            #is a new scene, add to database
            sceneNum+=1
            sceneTemp.append(Scene(text))
            print "_________________________________________________"
            print "Scene " + text
            print "_________________________________________________"
        else:
            sceneTemp[-1].dirs.append(text)
            print "\tDirection " + text
        
    #Character name
    elif (checkCharacter(text, indent)):
        #is a Character name, check if it's in the database with appropriate script & get new char_id
        lineNum+=1
        isLine=True
        characterNum = 3 #needs a call to database to find char_id
        print "\t\tCharacter: " + removeParentesis(text)

        charName = removeParentesis(text)
        if(not charName in sceneTemp[-1].chars):
            sceneTemp[-1].chars.append(charName)

    
    #Actual line, always immediately after a character name
    elif (isLine):
        isLine = False
        #add line to database with char_id = characterNum, line num and scene num each 
        print "\tLine: " + text
        if(charName in sceneTemp[-1].phrases):
            sceneTemp[-1].phrases[charName].append(text)
        else:
            sceneTemp[-1].phrases[charName] = []
            sceneTemp[-1].phrases[charName].append(text)
        if(charName in charTemp):
            charTemp[charName].append(text)
        else:
            charTemp[charName] = []
            charTemp[charName].append(text)
        
        

        
    return

TextBlock = namedtuple("TextBlock",["x","y","text"])

def GetScript(filename):
    global sceneNum
    global sceneTemp
    sceneNum+=1
    sceneTemp.append(Scene("START"))
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
        raise PDFTextExtractionNotAllowed
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
                print text
            except:
                temp=5  

                
                
                
                
        text.sort(key = lambda row:(-row.y))
                    
        for line in text:
            ParseLine(line.text, line.x)
    #print Temporary information
    
    print "\n________________________________________________________________"
    print "\t\tANALYSIS"
    print "\n"
    
    print "Number of Scenes: "+str(len(sceneTemp))
    print "Scenes\n"
    for s in sceneTemp:
        print s.name
    
    print "\nCharacters"
    for s in charTemp.keys():
        print s+" "+str(len(charTemp[s]))+" lines"
    
    print "\nLines"
    for s in charTemp.keys():
        print charTemp[s]
    return


#GetDatabase()
#GetScript("sources/Analyze_that.pdf")
GetScript("sources/TMNT.pdf")
