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

import syslog
from activity_trigger import *
from settings_reader import get_patterns, get_variable

def compare(pattern):
    # get the prefix for logging
    syslog_prefix = get_variable("SYSTEMVARIABLES", "syslog_prefix", "str")
    # get the patterns from the config
    patterns = get_patterns()
    # make the pattern list coming from the evaluation to a string
    pattern = "".join(pattern)
    # in case the string is in the patterns
    if pattern in patterns:
        # get the command from the patterns
        command = patterns[pattern]
        # build the log message
        log_message = f'{syslog_prefix} INFO: Pattern "{pattern}" detected and command {command} triggered.'
        # send the log message to syslog
        syslog.syslog(syslog.LOG_INFO, log_message)
        syslog.closelog()
        # trigger the function with the name from the pattern
        globals()[patterns[pattern]]()

    else:
        # build the log message
        log_message = f'{syslog_prefix} ERR: Pattern "{pattern}" not detected in config.'
        # send the log message to syslog
        syslog.syslog(syslog.LOG_ERR, log_message)
        syslog.closelog()
