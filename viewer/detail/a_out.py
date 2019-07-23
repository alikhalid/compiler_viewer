#!/usr/bin/python

from .logger import *
from .utils import find_file
import subprocess as sp
import os
import sys


def run_sp(cmd, out_file, to=0.01):
    return_code = 0
    with open(out_file, 'w') as f:
        p = sp.Popen(
            cmd.split(),
            stdout=f,
            stderr=f,
            universal_newlines=True)

        try:
            p.communicate(timeout=to)
        except sp.TimeoutExpired:
            p.kill()

    return True if not p.returncode else False


class Aout:
    def __init__(self, args):
        self.__build_dir = args['build_dir']
        self.__executable = args['executable']
        self.__out_file = args['out_txt']
        self.__init = False
        self.__logger = get_logger()

    def __delay_init(self):
        self.__init = True
        executable_file = find_file(self.__build_dir, self.__executable)
        self.__cmd = executable_file
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init Aout')
        self.__logger.info('\ta.out command: {}'.format(self.__cmd))

    def __call__(self):
        if not self.__init:
            self.__delay_init()

        self.__logger.info('Running Aout')
        return run_sp(self.__cmd, self.__out_file)
