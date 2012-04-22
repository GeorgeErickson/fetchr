#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pkgutil

import requests
import clint
from clint.textui import puts, colored, indent
from clint import resources
import yaml

sys.path.insert(0, os.path.abspath('..'))

def get_or_create_dotfile():
    resources.init('George Erickson', 'fetchr')
    config = resources.user.read('config.yaml')
    if not config:
        config = pkgutil.get_data('fetchr', 'data/config.yaml')
        print config
        resources.user.write('config.yaml', config)
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

