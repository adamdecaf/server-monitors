# Server Monitors
# Adam Shannnon
from twilio.rest import TwilioRestClient
from config import config
import subprocess
import os
import smtplib
from email.mime.text import MIMEText

def checkForProcess(processName):
    subprocess.call("ps ax | grep " + processName + " > " + config['runningProcessesFilePath'], shell=True)
    processesFile = open(config['runningProcessesFilePath']).read().split("\n")
    return processesFile

def isProcessRunning(processName):
    if (len(checkForProcess(processName)) > 3):
        return True
    else:
        return False

def sendToTwillo(processName):
    msg = "The process '" + processName + "' isn't running."
    client = TwilioRestClient(config['accountSID'], config['accountToken'])
    message = client.sms.messages.create(config['phoneTo'], config['phoneFrom'], msg)

def monitorProcess(processName):
    if not(isProcessRunning(processName)):
        sendToTwillo(processName)

# Here's a list of processes we're going to check
monitorProcess("httpd")
monitorProcess("mysqld")
monitorProcess("sshd")
monitorProcess("fah6")
monitorProcess("crond")
