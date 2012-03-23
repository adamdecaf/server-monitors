# Server Monitors
# Adam Shannnon
from twilio.rest import TwilioRestClient
from config import config
import subprocess
import os

subprocess.call("df > " + config['diskSpaceFilePath'], shell=True)
diskSpaceFile = open(config['diskSpaceFilePath']).read().split("\n")

i = 0
for line in diskSpaceFile:
    diskSpaceFile[i] = line.split(" ")
    i += 1

slash = diskSpaceFile[1]
tmp = diskSpaceFile[2]

# Print Off the messages
rootMsg = "\n"
tmpMsg = "\n"
if int(slash[19]) < config['lowRootSpace'] or int(tmp[32]) < config['lowTmpSpace']:

    # Check the stats for /
    rootMsg += "low disk space on: " + slash[0] + "\n"
    rootMsg += "mounted at: " + slash[22] + "\n"
    rootMsg += "total space: " + slash[13] + "\n"
    rootMsg += "free space: " + slash[19] + "\n"
    rootMsg += "used space: " + slash[16] + "\n"

    # Check the ststs for /tmp
    tmpMsg += "low disk space on: /" + tmp[0] + "\n"
    tmpMsg += "mounted at: " + tmp[36] + "\n"
    tmpMsg += "total space: " + tmp[19] + "\n"
    tmpMsg += "free space: " + tmp[32] + "\n"
    tmpMsg += "used space: " + tmp[28] + "\n"

    # Send through sendmail
    p = os.popen("%s -t" % config['sendmail'], "w")
    p.write("To: " + config['email']  + "\n")
    p.write("From: " + config['emailFrom'] + "\n")
    p.write("Subject: Warning: Low Disk Space (Amazon Box)\n\n")
    p.write(rootMsg + tmpMsg)
    p.close()

    # Now, send a text
    client = TwilioRestClient(config['accountSID'], config['accountToken'])
    message = client.sms.messages.create(config['phoneTo'], config['phoneFrom'], rootMsg)
    message = client.sms.messages.create(config['phoneTo'], config['phoneFrom'], tmpMsg)

else:
    print "All Good"
