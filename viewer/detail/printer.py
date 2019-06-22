#!/usr/bin/python

from logger import *
from parse_build_error import parse_build_error
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
        self._fname = os.path.join(os.getcwd(), '__viewer_cache__/cmp_exp')
        self._parse_error = parse_build_error()

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Output file: {}'.format(self._fname))

    def print_msg(self, success, msg=""):
        if success:
            self._print_success(msg)
        else:
            self._print_failure(self._parse_error(msg))

    def compiling(self):
        write_to_file(self._fname, 'Compiling...')

    def _print_success(self, msg):
        self._logger.info('Compilation successful')
        write_to_file(self._fname, "Compilation successful!\n{0}".format(msg))

    def _print_failure(self, msg):
        self._logger.info('Compilation failed')
        write_to_file(self._fname, "Compilation failed!\n{0}".format(msg))
