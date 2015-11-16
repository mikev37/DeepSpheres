'''
Created on Nov 2, 2015

@author: karl
'''
#!/usr/bin/python
import _mysql

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from ccm.Pages import Page
from libxml2 import lineNumbersDefault



  
def GetDatabase():
    dbPassword = "into0myheart"
    dbUser = "karl"
    dbHost = "localhost"
    dbName = "Plays"
    db=_mysql.connect(host=dbHost,user=dbUser,
                  passwd=dbPassword,db=dbName)
    if not db:
        print "didn't connect"
          
lineNum = 0   #initialize to 1 plus largest line_id in database
sceneNum = 0   #initialize to 1 plus largest scene_id in database
characterNum = 0   #set during parse, but can add new characters on the fly, using char_id
isLine = False


def ParseLine(text, indent):
    global lineNum
    global sceneNum
    global characterNum
    global isLine
    
    
    #Scene start
    if (indent>100 and indent<120):
        firstBit = text[:5]
        if (firstBit.isupper()):
            #is a new scene, add to database
            sceneNum+=1
            print "Scene " + text
        
    #Character name
    elif (text.isupper() and indent>200 and indent<300):
        #is a Character name, check if it's in the database with appropriate script & get new char_id
        lineNum+=1
        print "Character: " + text
        isLine=True
        characterNum = 3 #needs a call to database to find char_id
    
    #Actual line, always immediately after a character name
    elif (isLine):
        isLine = False
        #add line to database with char_id = characterNum, line num and scene num each 
        print "Line: " + text
        
    return

def GetScript(filename):
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
    laparams.boxes_flow = 1.0
    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        for page in layout:
            try:
                ParseLine(page.get_text(), page.x0)
            except:
                temp=5
    return


#GetDatabase()
#GetScript("sources/Analyze_that.pdf")
GetScript("sources/TMNT.pdf")
