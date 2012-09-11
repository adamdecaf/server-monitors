#SampleConfigFile
#AdamShannon

config = {}
config["diskSpaceFilePath"] = "/tmp/disk-space"
config["freeMemoryFilePath"] = "/proc/meminfo"
config['runningProcessesFilePath'] = "/tmp/running-processes"

config["weatherFile"] = "/tmp/weather"
config["weatherCity"] = "" # Put +'s where spaces should go

config["lowRootSpace"] = 2 * 1024 * 1024 # ~GB
config["lowTmpSpace"] = 2 * 100 * 1024 # ~200MB
config["lowFreeMemory"] = 7 * 1024 # 10MB

# These are the offsets for the split lines of the file
config["spacesOffset"] = 0
config["memoryTotal"] = 0
config["memoryFree"] = 0
config["swapTotal"] = 0
config["swapFree"] = 0

config['serverName'] = ""

config["sendmail"] = "/usr/sbin/sendmail"
config["email"] = ""
config["emailFrom"] = ""

config["phoneTo"] = ""
config["phoneFrom"] = ""

config["accountSID"] = ""
config["accountToken"] = ""
