#!/usr/bin/python

from logger import *
from watch_file_change import check_changes

import argparse as ap
import subprocess as sp
import os, time, sys

def read_file(fname):
    out = []
    with open(fname, 'r') as f:
        for line in f:
            out.append(line.strip())
    return out

def write_to_file(fname, out):
    with open(fname, 'w') as f:
        f.write(out)

def run_sp(cmd, wd=os.getcwd()):
    p = sp.Popen(cmd.split(), stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
    o, e = p.communicate()
    return (True, str(o)) if not p.returncode else (False, str(e))

class runner:
    def __init__(self, args):
        self._j = args['j']
        self._project_dir = args['project_dir']
        self._build_dir = os.path.join(self._project_dir, args['build_dir'])
        self._src_dir = os.path.join(self._project_dir, args['src_file_dir'])
        self._fname = os.path.join(os.getcwd(), '__viewer_cache__/cmp_exp')
        self._cmd = 'make -j{0}'.format(self._j)
        self._cc = check_changes(self._src_dir)
        self._logger = get_logger()

        self._chdir()
        self._log_info()

    def _chdir(self):
        self._wd = os.getcwd()
        os.chdir(self._build_dir)

    def _log_info(self):
        self._logger.info('Starting runner')
        self._logger.info('Project dir: {}'.format(self._project_dir))
        self._logger.info('Build dir: {}'.format(self._build_dir))
        self._logger.info('Src dir: {}'.format(self._src_dir))
        self._logger.info('Make cmd: {}'.format(self._cmd))
        self._logger.info('Changed cwd from: {0} to: {1}'.format(self._wd, os.getcwd()))

    def _print_msg(self, success, msg=""):
        if success:
            self._logger.info('Compilation successful')
            write_to_file(self._fname, "Compilation successful!")
        else:
            self._logger.info('Compilation failed')
            write_to_file(self._fname, "Compilation failed!\n{0}".format(msg))

    def run(self):
        while True:
            if self._cc.can_update():
                if self._cc.can_reset():
                    self._cc.reset()
                write_to_file(self._fname, 'Compiling...')
                passed, curr_out = run_sp(self._cmd)
                self._print_msg(passed, curr_out)

            time.sleep(1)

    def reset(self):
        self._logger.info('Resetting runner')
        os.chdir(self._wd)
        os.remove(self._fname)

def cmd_args():
    parser = ap.ArgumentParser()
    parser.add_argument('-d', '--project-dir', required=False, default=os.getcwd(), help='Project home dir')
    parser.add_argument('-b', '--build-dir', required=False, default='build', help='Dir with makefiles')
    parser.add_argument('-s', '--src-file-dir', required=False, default='', help='Source file dir')
    parser.add_argument('-j', required=False, default=1, help='-j option for make command')

    return  vars(parser.parse_args())

def main():
    args = cmd_args()
    init_logger()

    logger = get_logger()
    logger.info('Starting compiler viewer')
    logger.info('running from dir: {}'.format(os.getcwd()))

    while True:
        r = runner(args)
        try:
            r.run()
        except KeyboardInterrupt:
            logger.info("Exiting now")
        #except Exception as e:
        #    logger.info('Caught exception: {0}'.format(str(e.message)))
        #    r.reset()

if __name__ == '__main__':
    main()
