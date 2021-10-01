import os
import syslog
from settings_reader import get_variable

def reboot():
    # get the prefix for logging
    syslog_prefix = get_variable("SYSTEMVARIABLES","syslog_prefix", "str")
    # build the log message
    log_message = f'{syslog_prefix} INFO: Rebooting.'
    # send the log message to syslog
    syslog.syslog(syslog.LOG_INFO, log_message)
    syslog.closelog()
    # perform the task
    os.system('reboot')

def poweroff():
    # get the prefix for logging
    syslog_prefix = get_variable("SYSTEMVARIABLES","syslog_prefix", "str")
    # build the log message
    log_message = f'{syslog_prefix} INFO: Powering off.'
    # send the log message to syslog
    syslog.syslog(syslog.LOG_INFO, log_message)
    syslog.closelog()
    #perform the task
    os.system('poweroff')
