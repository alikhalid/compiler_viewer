#!/usr/bin/python

from .logger import *
import subprocess as sp
import os
import sys


def run_sp(cmd, wd=os.getcwd()):
    p = sp.run(
        cmd.split(),
        stderr=sp.PIPE,
        universal_newlines=True,
        cwd=wd)

    return (True, '') if not p.returncode else (False, str(p.stderr))


class Build:
    def __init__(self, args):
        self.__flags = ' '.join(args['build_flags'])
        self.__include_dir = '-I {}'.format(
            ' '.join(args['include_dir'])) if args['include_dir'] else ''
        self.__fname = args['example_cpp']
        self.__gcc_cmd = 'g++-9 {0} {1} {2} -o a.out'.format(
            self.__flags, self.__include_dir, self.__fname)

        self.__working_dir = args['build_dir']

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init Build')
        self.__logger.info('\tgcc_cmd: {}'.format(self.__gcc_cmd))
        self.__logger.info('\tworking_dir: {}'.format(self.__working_dir))

    def __call__(self):
        self.__logger.info('Running gcc')
        return run_sp(self.__gcc_cmd, self.__working_dir)
