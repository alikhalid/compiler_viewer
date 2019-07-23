#!/usr/bin/python

from .logger import *
from .utils import find_file
from enum import Enum
import subprocess as sp
import os
import sys
import glob


class Platform(Enum):
    MAC = 'darwin'
    LINUX = 'linux'


def run_sp(cmd):
    p = sp.run(
        cmd.split(),
        stdout=sp.PIPE,
        stderr=sp.PIPE,
        universal_newlines=True)

    return (
        True, str(
            p.stdout)) if not p.returncode else (
        False, str(
            p.stderr))


class Objdump:
    def __init__(self, args):
        self.__flags = ' '.join(args['objdump_flags'])
        self.__executable = args['executable']
        self.__build_dir = args['build_dir']
        self.__init = False
        self.__logger = get_logger()

    def __delay_init(self):
        self.__init = True
        executable_file = find_file(self.__build_dir, self.__executable)
        platform_specific_flags = '--insn-width=16 -M intel' if Platform(
            sys.platform) == Platform.LINUX else '-x86-asm-syntax=intel -no-leading-addr -no-leading-headers -no-show-raw-insn'
        self.__cmd = 'objdump {0} -l -C -d -S {1} {2}'.format(
            platform_specific_flags, self.__flags, executable_file)

        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init Objdump')
        self.__logger.info('\tObjdump cmd: {}'.format(self.__cmd))

    def __call__(self):
        if not self.__init:
            self.__delay_init()

        self.__logger.info('Running Objdump')
        return run_sp(self.__cmd)

