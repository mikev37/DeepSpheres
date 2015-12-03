from nltk.tag import pos_tag
import nltk.tokenize
from nltk.corpus import cmudict
from wordgen import gen_word
from nltk import pos_tag, ne_chunk
from nltk.tokenize import SpaceTokenizer
sentence = "who is Mahatma Gandhi visiting I'm HIS PRETTY GIRLFRIEND a Denny's McDonalds in broad daylight Shtruus"
tokenizer = SpaceTokenizer()
toks = tokenizer.tokenize(sentence)
pos = pos_tag(toks)
chunked_nes = ne_chunk(pos) 
print chunked_nes
nes = [' '.join(map(lambda x: x[0], ne.leaves())) for ne in chunked_nes if isinstance(ne, nltk.tree.Tree)]

print nes
'''
qry = "who is Mahatma Gandhi"
tokens = nltk.tokenize.word_tokenize(qry)
pos = nltk.pos_tag(tokens)
sentt = nltk.ne_chunk(pos, binary = False)
print sentt
person = []
for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
    for leave in subtree.leaves():
        person.append(leave)
print "person=", person
    
   ''' 
    
'''
d = cmudict.dict()
def nsyl(word):
  return [list(y for y in x if y[-1].isdigit()) for x in d[word.lower()]]

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
    sentence = sentence.replace(noun, "0x"+str(tokenlist.index(noun))+"x")
    #print nsyl(noun)
    
    
print sentence
 
for var in tokenlist:
    word = gen_word(2, 4)
    sentence = sentence.replace("0x"+str(tokenlist.index(var))+"x",word)
    
print sentence
'''