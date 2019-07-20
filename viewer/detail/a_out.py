#!/usr/bin/python

from .logger import *
import subprocess as sp
import os, sys

def run_sp(cmd, out_file, wd, to=3):
    with open(out_file, 'w') as f:
        p = sp.run(cmd.split(), stdout=f, stderr=f, universal_newlines=True, cwd=wd, timeout=to)
        return True if not p.returncode else False

class Aout:
    def __init__(self, args):
        self.__build_dir = args['build_dir']
        self.__cmd = './{}'.format(args['executable'])
        self.__out_file = args['out_txt']

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init Aout')

    def __call__(self):
        self.__logger.info('Running Aout')
        return run_sp(self.__cmd, self.__out_file, self.__build_dir)
