# server-monitors

This is a collection of scripts (and cron jobs) to setup some basic monitoring of servers.

Note: This is setup for the default amazon ami on an ec2 server. You may have to alter this to get it work perfectly on your server.

# Install

First, you must have python and twilio-python installed.

    sudo su
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    pip install twilio

Second, pull down the project and setup the cron jobs.

    git clone git@github.com:adamdecaf/server-monitors.git
    sudo su
    crontab -e

    * * * * * python /path/to/server-monitors/disk-space.py
    * * * * * python /path/to/server-monitors/free-memory.py
  
