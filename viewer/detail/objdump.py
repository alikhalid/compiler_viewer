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
        self._asm = args['asm']
        build_dir = os.path.join(args['project_dir'], args['build_dir'])
        self._obj_file = self._find_file(build_dir, args['obj_file'])
        self._cmd = 'objdump --insn-width=16 -l -C -d -S -M intel {0}'.format(self._obj_file)

        self._logger = get_logger()
        self._log_info()

    def __call__(self):
        return run_sp(self._cmd)

    def _find_file(self, directory, fname):
        all_files = get_all_files(directory, fname)
        if len(all_files) == 1:
            return all_files[0]

        self._asm = False
        return ''

    def _log_info(self):
        self._logger.info('objdump for file: {}'.format(self._obj_file))
        self._logger.info('objdump cmd: {}'.format(self._cmd))


#args = {'asm' : True, 'obj_file' : 'example.out', 'build_dir' : '/home/ali/temp/test_vim_viewer'}
