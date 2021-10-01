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
