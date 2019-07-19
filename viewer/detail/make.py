#!/usr/bin/python

from .logger import *
import subprocess as sp
import os
import sys


def run_sp(cmd, wd):
    p = sp.run(
        cmd.split(),
        stderr=sp.PIPE,
        universal_newlines=True,
        cwd=wd)

    return (True, '') if not p.returncode else (False, str(p.stderr))


class Make:
    def __init__(self, args):
        self.__flags = ' '.join(args['build_flags'])
        self.__build_dir = args['build_dir']
        self.__cmd = 'Make {}'.format(self.__flags)

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init Make')
        self.__logger.info('\tbuild dir for Make: {}'.format(self.__build_dir))
        self.__logger.info('\tMake cmd: {}'.format(self.__cmd))

    def __call__(self):
        self.__logger.info('Running Make')
        return run_sp(self.__cmd, self.__build_dir)
