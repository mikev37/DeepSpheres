import DataStructures
from Creation import createPlay
from Merging import mergeDB
from postprocess import replaceTokens
from PreProcess import tokenize
from PreProcess import computeVariance

lineA = DataStructures.LineObj("Hamlet",0,0,"DIRECTION","It was a sunny day")
lineB = DataStructures.LineObj("Hamlet",0,1,"JACKAL","Hello")
lineC = DataStructures.LineObj("Hamlet",0,2,"TERRY","Hi")
lineD = DataStructures.LineObj("Hamlet",0,3,"DIRECTION","It started raining, the McDonalds was wet")
lineE = DataStructures.LineObj("Hamlet",0,4,"TERRY","What wonderful weather, TERRY")
lineF = DataStructures.LineObj("Hamlet",0,5,"JACKAL","I can't believe it")
lineG = DataStructures.LineObj("Hamlet",0,6,"DIRECTION","JACKAL draws his sword")
lineAA = [None,lineA]
lineAB = [lineA,lineB]
lineBC = [lineB,lineC]
lineCD = [lineC,lineD]
lineDE = [lineD,lineE]
lineEF = [lineE,lineF]
lineFG = [lineF,lineG]
charA = DataStructures.CharacterObject("DIRECTION")
charB = DataStructures.CharacterObject("JACKAL")
charC = DataStructures.CharacterObject("TERRY")

charA.anger = .2
charB.anger = .2
charC.anger = .2

charC.lines = [lineBC,lineDE]
charB.lines = lin
#Pull charcters and scenes from all the Line

#tokenize the play and compute statistics

#merge play datas until there's only one

#
