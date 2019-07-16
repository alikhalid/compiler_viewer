#!/usr/bin/python

from logger import *
import subprocess as sp
import os, sys

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, cwd=wd)
    o, e = p.communicate()
    return (True, '') if not p.returncode else (False, str(e))

class AOut:
    def __init__(self, args):
        self.__build_dir = args['build_dir']
        self.__cmd = './a.out > out'

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init AOut')

    def __call__(self):
        self.__logger.info('Running AOut')
        return run_sp(self.__cmd, 'viewer/__viewer_cache__')
