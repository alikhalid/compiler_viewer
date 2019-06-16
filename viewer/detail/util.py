#!/usr/bin/python

import os

def read_file(fname):
    out = []
    with open(fname, 'r') as f:
        for line in f:
            out.append(line.strip())
    return out

def write_to_file(fname, out):
    with open(fname, 'w') as f:
        f.write(out)

