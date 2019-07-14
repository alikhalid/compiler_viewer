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
        self._args = args
        self._watch_dirs = args['watch_dirs']
        self._all_files = get_all_files(self._watch_dirs)
        self._num_files = len(self._all_files)
        self._modified_files = self._all_files
        self._files_mtime = {k: 0 for k in self._all_files}
        self._files_md5 = {k: 0 for k in self._all_files}

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Init watch_file_change')
        self._logger.info('\tWorking dir: {}'.format(self._watch_dirs))

    def can_update(self):
        if self._mtime_check() and self._md5_check():
            if self._can_reset:
                self._reset
            return True

        return False

    def _reset(self):
        self._logger.info("Number of files changed resetting state")
        self.__init__(self._args)

    def _can_reset(self):
        num_files = len(get_all_files(self._watch_dirs))
        return num_files != self._num_files

    def _mtime_check(self):
        files_mtime = self._get_mtime()
        self._logger.debug(
            '_mtime_check:::files_mtime: {}'.format(files_mtime))
        changed = False
        if files_mtime != self._files_mtime:
            self._logger.info('mtime changed')
            changed = True
            self._modified_files = diff_dicts(files_mtime, self._files_mtime)
            self._logger.debug(
                '_mtime_check::self._modified_files: {}'.format(
                    self._modified_files))
            self._update_files_mtime(files_mtime)

        return changed

    def _get_mtime(self):
        data = {}
        for f in self._all_files:
            data[f] = os.path.getmtime(f)

        return data

    def _update_files_mtime(self, update_from):
        for f in self._modified_files:
            self._files_mtime[f] = update_from[f]

        self._logger.debug(
            '_update_files_mtime::self._files_mtime: {}'.format(
                self._files_mtime))

    def _md5_check(self):
        files_md5 = self._get_md5()
        self._logger.debug('_md5_check::files_md5: {}'.format(files_md5))
        changed = False
        if self._can_update_md5(files_md5):
            self._logger.info('md5 changed')
            changed = True
            self._update_files_md5(files_md5)
            self._reset_modified_files()

        return changed

    def _get_md5(self):
        data = {}
        for f in self._all_files:
            data[f] = hashlib.md5(open(f, 'rb').read()).hexdigest()

        return data

    def _update_files_md5(self, update_from):
        for f in self._modified_files:
            self._files_md5[f] = update_from[f]

        self._logger.debug(
            '_update_files_mdf::self._files_md5: {}'.format(
                self._files_md5))

    def _can_update_md5(self, files_md5):
        for k, v in list(files_md5.items()):
            if self._files_md5[k] != v:
                return True

        return False

    def _reset_modified_files(self):
        self._modified_files = []
