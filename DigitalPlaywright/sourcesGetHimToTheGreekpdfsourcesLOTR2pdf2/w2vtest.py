
import os
print os.getcwd()
print "["
for file in os.listdir(os.getcwd()):
    print '"'+ file+'",'
    
print "]"
#word2vec.word2phrase('C:\devbox\DeepSphere\word2vec\text8', 'C:\devbox\DeepSphere\word2vec\text8-phrases', verbose=True)