#!/usr/bin/python

from logger import *
from parse_error import parse_error
from parse_asm import parse_asm

import os

def read_file(fname):
    out = []
    with open(fname, 'r') as f:
        for line in f:
            out.append(line.strip())
    return out

def write_to_file(fname, out):
    with open(fname, 'w') as f:
        f.write(out)

class printer:
    def __init__(self):
        self._fname = os.path.join(os.getcwd(), 'viewer/__viewer_cache__/cmp_exp')
        self._parse_error = parse_error()
        self._parse_asm = parse_asm()

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Output file: {}'.format(self._fname))

    def print_msg(self, success, msg=""):
        if success:
            self._print_success(msg)
        else:
            self._print_failure(msg)

    def compiling(self):
        write_to_file(self._fname, 'Compiling...')

    def _print_success(self, msg):
        self._logger.info('Compilation successful')
        parsed_msg = msg
        if msg:
            parsed_msg = self._parse_asm(msg)
        write_to_file(self._fname, "Compilation successful!\n{0}".format(parsed_msg))

    def _print_failure(self, msg):
        self._logger.info('Compilation failed')
        try:
            parsed_msg = self._parse_error(msg)
        except:
            self._logger.error('Unable to parse compiler error!')
            parsed_msg = msg
        write_to_file(self._fname, "Compilation failed!\n{0}".format(parsed_msg))
