from nltk.tag import pos_tag
from nltk.corpus import cmudict
from wordgen import gen_word
tokenlist = []
tokendict = {}
'''
d = cmudict.dict()
def nsyl(word):
  return [list(y for y in x if y[-1].isdigit()) for x in d[word.lower()]]
'''
sentence = "Michael Jackson likes to eat at McDonalds"
tagged_sent = pos_tag(sentence.split())
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]
print sentence
propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
#print propernouns
# ['Michael','Jackson', 'McDonalds']

for noun in propernouns:
    if noun not in tokenlist:
        tokenlist.append(noun)
    sentence = sentence.replace(noun, "0x"+str(tokenlist.index(noun)))
    #print nsyl(noun)
    
    
print sentence
 
for var in tokenlist:
    word = gen_word(2, 4)
    sentence = sentence.replace("0x"+str(tokenlist.index(var)),word)
    
print sentence