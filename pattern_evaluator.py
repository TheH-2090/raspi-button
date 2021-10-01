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
