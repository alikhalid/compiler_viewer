#!/usr/bin/python

from logger import *
import subprocess as sp
import os, sys

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, cwd=wd)
    o, e = p.communicate()
    return (True, '') if not p.returncode else (False, str(e))

class build:
    def __init__(self, args):
        self._args = ' '.join(args['flags'])
        self._include_dir = ''
        if args['include_dir']:
            self._include_dir = '-I {}'.format(' '.join(args['include_dir']))
        self._fname = 'example.cpp'
        self._gcc_cmd = 'g++ {0} {1} {2}'.format(self._args, self._include_dir, self._fname)

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Init build')
        self._logger.info('\tgcc_cmd: {}'.format(self._gcc_cmd))

    def __call__(self):
        self._logger.info('Running gcc')
        return run_sp(self._gcc_cmd, '__viewer_cache__')
