import configparser

# setup the configparser and read the config
config = configparser.ConfigParser()
config.read('config.ini')

def get_patterns():
    # build a dictionary from the section containing the patterns
    section = 'PATTERNS'
    patterns = {}
    for eachPattern in config[section]:
        patterns[eachPattern] = config[section][eachPattern]
    return patterns

def get_variable(section, variable, type):
    # get a single variable from the config assign it the desired data type
    if type == 'int':
        return int(config.get(section, variable))
    elif type == 'float':
        return float(config.get(section, variable))
    elif type == 'bool':
        return bool(config.get(section, variable))
    else:
        return str(config.get(section, variable))
