# server-monitors

This is a collection of scripts (and cron jobs) to setup some basic monitoring of servers.

# Install

First, you must have python and twilio-python installed.

    sudo su
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    pip install twilio

Second, pull down the project and setup the cron jobs.

    git clone git@github.com:adamdecaf/server-monitors.git
    crontab -e
  
