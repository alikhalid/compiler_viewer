#!/usr/bin/python

from .logger import *
import os
import subprocess
import glob
import hashlib


def get_all_files(dirs):
    pattern = ('.hpp', '.cpp', '.h', '.c', '.cxx')
    all_files = []

    for directory in dirs:
        for base, _, fnames in os.walk(directory):
            for fname in fnames:
                if fname.endswith(pattern):
                    all_files.append(os.path.join(base, fname))

    return all_files


def diff_dicts(a, b):
    diff = []
    for k, v in list(a.items()):
        if v != b[k]:
            diff.append(k)

    return diff


class check_changes:
    def __init__(self, args):
        self.__args = args
        self.__watch_dirs = args['watch_dirs']
        self.__all_files = get_all_files(self.__watch_dirs)
        self.__num_files = len(self.__all_files)
        self.__modified_files = self.__all_files
        self.__files_mtime = {k: 0 for k in self.__all_files}
        self.__files_md5 = {k: 0 for k in self.__all_files}

        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init watch_file_change')
        self.__logger.info('\tWorking dir: {}'.format(self.__watch_dirs))

    def can_update(self):
        if self.__mtime_check() and self.__md5_check():
            if self.__can_reset:
                self.__reset
            return True

        return False

    def __reset(self):
        self.__logger.info("Number of files changed resetting state")
        self.___init__(self.__args)

    def __can_reset(self):
        num_files = len(get_all_files(self.__watch_dirs))
        return num_files != self.__num_files

    def __mtime_check(self):
        files_mtime = self.__get_mtime()
        self.__logger.debug(
            '_mtime_check:::files_mtime: {}'.format(files_mtime))
        changed = False
        if files_mtime != self.__files_mtime:
            self.__logger.info('mtime changed')
            changed = True
            self.__modified_files = diff_dicts(files_mtime, self.__files_mtime)
            self.__logger.debug(
                '_mtime_check::self.__modified_files: {}'.format(
                    self.__modified_files))
            self.__update_files_mtime(files_mtime)

        return changed

    def __get_mtime(self):
        data = {}
        for f in self.__all_files:
            data[f] = os.path.getmtime(f)

        return data

    def __update_files_mtime(self, update_from):
        for f in self.__modified_files:
            self.__files_mtime[f] = update_from[f]

        self.__logger.debug(
            '_update_files_mtime::self.__files_mtime: {}'.format(
                self.__files_mtime))

    def __md5_check(self):
        files_md5 = self.__get_md5()
        self.__logger.debug('_md5_check::files_md5: {}'.format(files_md5))
        changed = False
        if self.__can_update_md5(files_md5):
            self.__logger.info('md5 changed')
            changed = True
            self.__update_files_md5(files_md5)
            self.__reset_modified_files()

        return changed

    def __get_md5(self):
        data = {}
        for f in self.__all_files:
            data[f] = hashlib.md5(open(f, 'rb').read()).hexdigest()

        return data

    def __update_files_md5(self, update_from):
        for f in self.__modified_files:
            self.__files_md5[f] = update_from[f]

        self.__logger.debug(
            '_update_files_mdf::self.__files_md5: {}'.format(
                self.__files_md5))

    def __can_update_md5(self, files_md5):
        for k, v in list(files_md5.items()):
            if self.__files_md5[k] != v:
                return True

        return False

    def __reset_modified_files(self):
        self.__modified_files = []
