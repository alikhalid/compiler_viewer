#!/usr/bin/python

from .logger import *
import subprocess as sp
import os
import sys


def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(
        cmd.split(),
        stdout=sp.PIPE,
        stderr=sp.PIPE,
        universal_newlines=True,
        cwd=wd)
    o, e = p.communicate()
    return (True, '') if not p.returncode else (False, str(e))
    # return (True, str(o)) if not p.returncode else (False, str(e))


class make:
    def __init__(self, args):
        self.__flags = ' '.join(args['build_flags'])
        self.__build_dir = args['build_dir']
        self.__cmd = 'make {}'.format(self.__flags)

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init make')
        self.__logger.info('\tbuild dir for make: {}'.format(self.__build_dir))
        self.__logger.info('\tmake cmd: {}'.format(self.__cmd))

    def __call__(self):
        self.__logger.info('Running make')
        return run_sp(self.__cmd, self.__build_dir)
