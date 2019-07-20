#!/usr/bin/python

from .logger import *
from .parse_error import ParseError
from .parse_asm import ParseAsm

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


class Printer:
    def __init__(self, args):
        self.__fname = args['cmp_exp']
        self.__parse_error = ParseError(args)
        self.__parse_asm = ParseAsm(args)

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info("Init Printer")
        self.__logger.info('\tOutput file: {}'.format(self.__fname))

    def print_msg(self, success, msg=""):
        if success:
            self.__print_success(msg)
        else:
            self.__print_failure(msg)

    def compiling(self):
        write_to_file(self.__fname, 'Compiling...')

    def __print_success(self, msg):
        self.__logger.info('Compilation successful')
        parsed_msg = msg
        if msg:
            try:
                parsed_msg = self.__parse_asm(msg)
            except BaseException:
                self.__logger.error('Unable to parse assemby!')
                parsed_msg = msg
        write_to_file(
            self.__fname,
            "Compilation successful!\n{0}".format(parsed_msg))

    def __print_failure(self, msg):
        self.__logger.info('Compilation failed')
        try:
            parsed_msg = self.__parse_error(msg)
        except BaseException:
            self.__logger.error('Unable to parse compiler error!')
            parsed_msg = msg
        write_to_file(
            self.__fname,
            "Compilation failed!\n{0}".format(parsed_msg))
