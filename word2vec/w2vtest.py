import word2vec
import os
print os.getcwd()
for file in os.listdir(os.getcwd()):
    print file
word2vec.word2phrase('C:\devbox\DeepSphere\word2vec\text8', 'C:\devbox\DeepSphere\word2vec\text8-phrases', verbose=True)