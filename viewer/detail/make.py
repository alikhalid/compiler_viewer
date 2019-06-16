#!/usr/bin/python

from logger import *
import subprocess as sp
import os, sys

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, cwd=wd)
    o, e = p.communicate()
    return (True, str(o)) if not p.returncode else (False, str(e))

class make:
    def __init__(self, args):
        self._build_dir = os.path.join(args['project_dir'], args['build_dir'])
        self._j = args['j']
        self._cmd = 'make -j{0}'.format(self._j)

        self._logger = get_logger()
        self._log_info()

    def __call__(self):
        return run_sp(self._cmd, self._build_dir)

    def _log_info(self):
        self._logger.info('build dir for make: {}'.format(self._build_dir))
        self._logger.info('-j option for make: {}'.format(self._j))
        self._logger.info('make cmd: {}'.format(self._cmd))
