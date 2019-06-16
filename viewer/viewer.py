#!/usr/bin/python

import argparse as ap
import subprocess as sp
import os, time

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
        self.j = args['j']
        self.build_dir = args['build_dir']
        self.fname = os.path.join(os.getcwd(), 'cmp_exp')
        self.cmd = 'make -j{0}'.format(self.j)

        os.chdir(self.build_dir)

    def print_msg(self, success, msg=""):
        if success:
            write_to_file(self.fname, "Compilation successful!")
        else:
            write_to_file(self.fname, "Compilation failed!\n{0}".format(msg))

    def run(self):
        while True:
            time.sleep(1)
            passed, curr_out = run_sp(self.cmd)
            self.print_msg(passed, curr_out)

    def clean(self):
        os.remove(self.fname)

def main():
    parser = ap.ArgumentParser()
    parser.add_argument('-d', '--build-dir', required=False, default=os.getcwd(), help='Directory with make files')
    parser.add_argument('-j', required=False, default=1, help='-j option for make command')
    args = vars(parser.parse_args())

    r = runner(args)
    try:
        r.run()
        r.clean()
    except KeyboardInterrupt:
        print("Exiting now")

if __name__ == '__main__':
    main()
