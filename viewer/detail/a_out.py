#!/usr/bin/python

from logger import *
import subprocess as sp
import os, sys

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, cwd=wd)
    o, e = p.communicate()
    return (True, '') if not p.returncode else (False, str(e))

class a_out:
    def __init__(self, args):
        self._build_dir = args['build_dir']
        self._cmd = './a.out > out'

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Init a_out')

    def __call__(self):
        self._logger.info('Running a_out')
        return run_sp(self._cmd, 'viewer/__viewer_cache__')
