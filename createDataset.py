import pandas as pd
import numpy as np
import os
import re
from datetime import datetime

personName = input('Enter your name: ')
waData = input('Do you have Whatsapp data to parse through (y/n)?')

def getWhatsappData():
    responseDictionary = dict()
    fbFile = open('Eva.txt', 'r',encoding='utf-8') 
    content = fbFile.readlines()
    myMessage, otherPersonsMessage, currentSpeaker = "","",""
    for index,lines in enumerate(content):
        dash = lines.find('-') + 2
        justMessage = lines[dash:]
        colon = justMessage.find(':')
        if(justMessage[:colon] == personName):
            if not myMessage:
                startMessageIndex = index - 1
            myMessage += justMessage[colon+2:]
        elif myMessage:
            for counter in range(startMessageIndex, 0, -1):
                currentLine = content[counter]
                dash = currentLine.find('-') + 2
                justMessage = currentLine[dash:]
                colon = justMessage.find(':')
                if not currentSpeaker:
                    currentSpeaker = justMessage[:colon]
                elif (currentSpeaker != justMessage[:colon] and otherPersonsMessage):
                    otherPersonsMessage = cleanMessage(otherPersonsMessage)
                    myMessage = cleanMessage(myMessage)
                    responseDictionary[otherPersonsMessage] = myMessage
                    break
                otherPersonsMessage = justMessage[colon+2:] + otherPersonsMessage
            myMessage, otherPersonsMessage, currentSpeaker = "","",""
        return responseDictionary
	
def cleanMessage(message):
	# Remove new lines within message
    cleanedMessage = message.replace('\n',' ').lower()
	# Deal with some weird tokens
    cleanedMessage = cleanedMessage.replace("\xc2\xa0", "")
	# Remove punctuation
    cleanedMessage = re.sub('([.,!?])','', cleanedMessage)
	# Remove multiple spaces in message
    cleanedMessage = re.sub(' +',' ', cleanedMessage)
    return cleanedMessage

combinedDictionary = {}
	
if (waData == 'y'):
    print ('Getting Whatsapp Data')
    combinedDictionary.update(getWhatsappData())
	
print('Total len of dictionary', len(combinedDictionary))

print('Saving conversation data dictionary')
np.save('conversationDictionary.npy', combinedDictionary)

conversationFile = open('conversationData.txt', 'w',encoding='utf-8')
for key,value in combinedDictionary.items():
    if (not key.strip() or not value.strip()):
            continue
    conversationFile.write(key.strip() + value.strip())
