#!/usr/bin/python

from logger import *
import os, subprocess, glob, hashlib

def get_all_files(directory):
    pattern = ('.hpp', '.cpp')
    all_files = []
    for base, _, fnames in os.walk(directory):
        for fname in fnames:
            if fname.endswith(pattern):
                all_files.append(os.path.join(base, fname))

    return all_files

def diff_dicts(a, b):
    diff = []
    for k, v in a.items():
        if v != b[k]:
            diff.append(k)

    return diff

class chanck_changes:
    def __init__(self, directory):
        self._wd = directory
        self._all_files = get_all_files(self._wd)
        self._num_files = len(self._all_files)
        self._modified_files = self._all_files
        self._files_mtime = {k : 0 for k in self._all_files}
        self._files_md5 = {k : 0 for k in self._all_files}

        self._logger = get_logger()

    def reset(self):
        self._logger.info("Number of files changed resetting state")
        self.__init__(self._wd)

    def can_reset(self):
        num_files = len(get_all_files(self._wd))
        return local_num_files != self._num_files

    def can_update(self):
        return True if self._mtime_check() and self._md5_check() else False

    def _mtime_check(self):
        files_mtime = self._get_mtime()
        changed = False
        if files_mtime != self._files_mtime:
            self._logger.info('mtime changed')
            changed = True
            self._modified_filed = diff_dicts(files_mtime, self._files_mtime)
            self._update_files_mtime(files_mtime)

        return changed

    def _get_mtime(self):
        data = {}
        for f in self._all_files:
            data[f] = os.path.gettime(f)

        return data

    def _update_files_mtime(self, update_from):
        for f in self._modified_files:
            self._files_mtime = update_from[f]

    def _md5_check(self):
        files_md5 = self._get_md5()
        changed = False
        if self._can_update_md5():
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
            self._files_mtime = update_from[f]

    def _can_update_md5(self, files_md5):
        for k, v in files_md5:
            if self._files_md5[k] != v:
                return True

        return False

    def _reset_modified_files(self):
        self._modified_files = []





















