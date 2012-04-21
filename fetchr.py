#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

import requests
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

def write_file(content, lib_data):
    file_path = os.path.join(os.getcwd(), lib_data.get('file_name'))
    with open(file_path, 'w+') as library_file:
        library_file.write(content)

def download(library_args_list, defined_libs):
    for lib in library_args_list:
        lib_data = defined_libs.get(lib, None)
        if lib_data:
            puts(colored.green('downloading %(file_name)s' % lib_data))
            library = requests.get(lib_data.get('url'))
            write_file(library.text, lib_data)
        else:
            puts(colored.red('%s not in config file' % lib))

def parse_arguments(args, defined_libs):
    if args.contains('-a'):
        #add new library
        pass
    elif args.contains('-e'):
        #edit library
        pass
    else:
        #actually download
        download(args.not_files.all, defined_libs)


def main(args=None):
    defined_libs = get_or_create_dotfile()
    if args:
        parse_arguments(args, defined_libs)
    else:
        #usage info
        puts('Usage: fetchr library libary2 ... \n')
        puts('Availible Libraries:')
        with indent(4):
            for display_name, lib in defined_libs.items():
                puts('%s: %s' % (display_name, lib.get('url')))
        puts('\nExample: fetchr underscore backbone')
        puts('downloads underscore and backbone to the current directory')

if __name__ == '__main__':
    main(args=clint.args)

