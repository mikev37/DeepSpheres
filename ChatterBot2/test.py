from chatterbot import ChatBot
import time

bot1 = ChatBot("Chicken")
bot2 = ChatBot("Duck")
bot1.gg()
bot1 = ChatBot("Chicken")
bot1.train("chatterbot.corpus.english")
bot2.train("chatterbot.corpus.test")
#bot1.train("chatterbot.corpus.test")
response2="What's slappin'?"
count = 0
count2 = 0
chicken = 1
if chicken==1:
    while True:
        count = count + 1
        time.sleep(2)
        response1=bot1.get_response(response2)
        if len(response1)<50:
            response1=response1+" "+bot1.get_response(response1)
        response2=bot2.get_response(response1)
        print "Bot1:"+response1
        time.sleep(2)
        print "Bot2:"+response2
elif chicken==2:
    while True:
        response1=bot1.get_response(raw_input(" "))
        print response1
elif chicken==3:
    i = 0
    while i < 50:
        response1=bot1.get_response("absolutely I agree with the")
        print response1
        if(response1 == "Hello"):
            count = count + 1
        else : count2 = count2 + 1
        i = i + 1
        
print "Hello " + str(count)
print "What a fag " + str(count2)

            
    
    