#!/usr/bin/python

from logger import *
import subprocess as sp
import os, sys

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, cwd=wd)
    o, e = p.communicate()
    return (True, '') if not p.returncode else (False, str(e))
    #return (True, str(o)) if not p.returncode else (False, str(e))

class make:
    def __init__(self, args):
        self._flags = ' '.join(args['build_flags'])
        self._build_dir = args['build_dir']
        self._cmd = 'make {}'.format(self._flags)

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Init make')
        self._logger.info('\tbuild dir for make: {}'.format(self._build_dir))
        self._logger.info('\tmake cmd: {}'.format(self._cmd))

    def __call__(self):
        self._logger.info('Running make')
        return run_sp(self._cmd, self._build_dir)

