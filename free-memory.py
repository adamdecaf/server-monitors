# Server Monitors
# Adam Shannon
from twilio.rest import TwilioRestClient
from config import config
import subprocess
import os

freeMemoryFile = open(config['freeMemoryFilePath']).read().split("\n")

i = 0
for line in freeMemoryFile:
    freeMemoryFile[i] = line.split(" ")
    i += 1

memoryTotal = int(freeMemoryFile[0][-2])
memoryFree = int(freeMemoryFile[1][-2])
swapTotal = int(freeMemoryFile[17][-2])
swapFree = int(freeMemoryFile[18][-2])

swapMsg = ""
freeMsg = ""
if swapTotal > 0 or swapFree > 0 or memoryFree < config['lowFreeMemory']:
    swapTotal = str(swapTotal)
    swapFree = str(swapFree)
    memoryTotal = str(memoryTotal)
    memoryFree = str(memoryFree)

    # Create the free message
    freeMsg += "total memory: " + memoryTotal + "\n"
    freeMsg += "free memory: " + memoryFree + "\n"
    
    # Create the swap message
    swapMsg += "total swap: " + swapTotal + "\n"
    swapMsg += "used swap: " + swapFree + "\n"

    # Send through sendmail
    p = os.popen("%s -t" % config['sendmail'], "w")
    p.write("To: " + config['email']  + "\n")
    p.write("From: " + config['emailFrom'] + "\n")
    p.write("Subject: Warning: Low Memory (Amazon Box)\n\n")
    p.write(freeMsg + swapMsg)
    p.close()

    # Now, send a text
    client = TwilioRestClient(config['accountSID'], config['accountToken'])
    message = client.sms.messages.create(config['phoneTo'], config['phoneFrom'], freeMsg)
    message = client.sms.messages.create(config['phoneTo'], config['phoneFrom'], swapMsg)

else:
    print "All Good"
