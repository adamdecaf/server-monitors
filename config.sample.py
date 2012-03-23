#SampleConfigFile
#AdamShannon

config={}
config["diskSpaceFilePath"] = "/tmp/disk-space"
config["freeMemoryFilePath"] = "/proc/meminfo"
config["lowRootSpace"] = 2 * 1024 * 1024 # ~GB
config["lowTmpSpace"] = 2 * 100 * 1024 # ~200MB

config["sendmail"] = "/usr/sbin/sendmail"
config["email"] = ""
config["emailFrom"] = ""

config["phoneTo"] = ""
config["phoneFrom"] = ""

config["accountSID"] = ""
config["accountToken"] = ""
