#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

import clint
from clint.textui import puts, colored, indent
import yaml

sys.path.insert(0, os.path.abspath('..'))

def get_or_create_dotfile():
    home_path = os.path.expanduser('~/')
    dotfile_path = os.path.join(home_path, '.fetchr')
    config_path = os.path.join(dotfile_path, 'config.yaml')
    default_dotfile_path = os.path.abspath('.fetchr')
    
    #can't find the config file so create it
    if not os.path.exists(config_path):
        shutil.copytree(default_dotfile_path, dotfile_path)
    
    with open(config_path) as config_file:
        config = config_file.read()
    
    try:
        return yaml.load(config)
    except yaml.parser.ParserError as e:
        puts(colored.red('Misconfigured config file, check %s' % config_path))
        with indent(4):
            puts(str(e))
        sys.exit(1)

def main(args=None):
    config_dict = get_or_create_dotfile()
    libs_files = config_dict.get('files')
    if args:
        pass
    else:
        puts('Usage: fetchr library libary2 ... \n')
        puts('Availible Libraries:')
        with indent(4):
            for lib in libs_files:
                puts('%(name)s: %(url)s' % lib)
        puts('\nExample: fetchr underscore backbone')
        puts('Will download the javascript files for underscore and backbone to the current directory')

if __name__ == '__main__':
    main(args=clint.args)

