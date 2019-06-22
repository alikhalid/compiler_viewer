#!/usr/bin/python

from logger import *
import subprocess as sp
import os, sys, glob

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, cwd=wd)
    o, e = p.communicate()
    return (True, str(o)) if not p.returncode else (False, str(e))

def get_all_files(directory, name):
    all_files = []
    for base, _, fnames in os.walk(directory):
        for fname in fnames:
            if fname.endswith(name):
                all_files.append(os.path.join(base, fname))

    return all_files

class objdump:
    def __init__(self, args):
        self._flags = ' '.join(args['objdump_flags'])
        self._init = False
        self._args = args
        self._logger = get_logger()

    def _delay_init(self):
        self._init = True
        build_dir = self._args['build_dir']
        self._obj_file = self._find_file(build_dir, self._args['asm'])
        self._cmd = 'objdump --insn-width=16 -l -C -d -S -M {0} intel {1}'.format(self._flags, self._obj_file)

        self._log_info()

    def _log_info(self):
        self._logger.info('Init objdump')
        self._logger.info('\tobjdump cmd: {}'.format(self._cmd))

    def __call__(self):
        if not self._init:
            self._delay_init()

        self._logger.info('Running objdump')
        return run_sp(self._cmd)

    def _find_file(self, directory, fname):
        all_files = get_all_files(directory, fname)
        if len(all_files) == 1:
            return all_files[0]

        assert False, 'Expected to find the file to generate assembly for'
