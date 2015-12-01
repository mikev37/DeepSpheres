from nltk.tag import pos_tag

tokenlist = []
tokendict = {}

sentence = "Michael Jackson likes to eat at McDonalds"
tagged_sent = pos_tag(sentence.split())
# [('Michael', 'NNP'), ('Jackson', 'NNP'), ('likes', 'VBZ'), ('to', 'TO'), ('eat', 'VB'), ('at', 'IN'), ('McDonalds', 'NNP')]

propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
print propernouns
# ['Michael','Jackson', 'McDonalds']

for noun in propernouns:
    if noun not in tokenlist:
        tokenlist.append(noun)
    sentence = sentence.replace(noun, "0x"+str(tokenlist.index(noun)))

print sentence

