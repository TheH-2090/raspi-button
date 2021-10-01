#!/bin/env python3

'''
    raspi-button.py | Customise the trigger actions of a button on a [PiCase].
    Copyright (C) 2021  https://github.com/TheH-2090

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, visit https://www.gnu.org/licenses/
'''

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
