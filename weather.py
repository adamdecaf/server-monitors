# Server Monitors
# Adam Shannnon
from twilio.rest import TwilioRestClient
from xml.dom.minidom import parse
from config import config
import subprocess
import os

subprocess.call("wget -O " + config['weatherFile'] + " 'http://www.google.com/ig/api?weather=" + config['weatherCity'] + "';", shell=True)
xmlFile = parse(config['weatherFile'])

def getValue(elmName, attribute = "data"):
    return xmlFile.getElementsByTagName(elmName)[0].getAttribute(attribute)

city = getValue("city")
date = getValue("forecast_date")
dayOfWeek = getValue("day_of_week")
high = getValue("high")
low = getValue("low")
wind = getValue("wind_condition")
condition = getValue("condition")

msg = "The weather for " + city + " on " + dayOfWeek + " " + date +  " looks to be " + condition
msg = msg + " and between " + high + " and " + low + " with a wind of " + wind

client = TwilioRestClient(config['accountSID'], config['accountToken'])
message = client.sms.messages.create(config['phoneTo'], config['phoneFrom'], msg)

