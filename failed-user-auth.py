# Server Monitors
# Adam Shannon
from config import config
import subprocess
import os

authLogFile = open(config["authLogFilePath"]).read().split("\n")
authMsg = ""

for line in authLogFile:
    if "invalid user" in line:
        # Add to the message
        authMsg += line + "\n"

# Send through sendmail
p = os.popen("%s -t" % config['sendmail'], "w")
p.write("To: " + config['email']  + "\n")
p.write("From: " + config['emailFrom'] + "\n")
p.write("Subject: [Security] " + config['serverName'] + " failed ssh logins\n\n")
p.write("Failed logins: \n\n" + authMsg)
p.close()

