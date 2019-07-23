#!/usr/bin/python

import os


def get_all_files(directory, name):
    all_files = []
    for base, _, fnames in os.walk(directory):
        for fname in fnames:
            if fname.endswith(name):
                all_files.append(os.path.join(base, fname))

    return all_files


def find_file(directory, fname):
    all_files = get_all_files(directory, fname)
    if len(all_files) == 1:
        return all_files[0]

    assert False, 'Expected to find the file to generate assembly for'
