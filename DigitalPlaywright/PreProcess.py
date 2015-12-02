'''
PreProcessing------------------------------------------

All names saved in an object
    Name : String
    All lines : String
    Lines : [Line]
    
Array of names contains all these objects

Each time a name is found in the line text, their name is replaced by 0m[index in name array]m

Tokens are essentially treated as names
    Token : String
    All lines : String
    Lines : [Line]

After processing for all the names, all the proper nouns are replaced by 0x[index of proper noun in array]x

Line object 
    name : CharObject
    Call : String
    Responce : String

All Scene headings get saved in an object

SceneObj
    Length of Scene as proportion of Play 0 to 1
    Start of scene as porportion of Play 0 to 1
    names contained
    Tokens contained
    
'''
import DataStructures
from nltk.tag import pos_tag
from nltk.corpus import cmudict
from wordgen import gen_word

'''
takes in a line 
replaces all name names with 0m[]m
replaces all tokens with 0x[]x
'''
def tokenize(sentence,tokenList,nameList):
    
    tagged_sent = pos_tag(sentence.split())
    
    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
    for noun in propernouns:
        if noun in nameList:
            sentence = sentence.replace(noun, "0m"+str(nameList.index(noun))+"m0")
    for noun in propernouns:
        if noun not in tokenList:
            tokenList.append(noun)
        sentence = sentence.replace(noun, "0x"+str(tokenList.index(noun))+"x0")

