#!/usr/bin/python

from detail import *
import argparse as ap
import os, time

class runner:
    def __init__(self, args):
        self._logger = get_logger()
        self._log_info()

        self._printer = printer()
        self._cc = check_changes(args)
        self._make = make(args)

        self._generate_asm = args['asm']
        if self._generate_asm:
            self._objdump = objdump(args)

    def _log_info(self):
        self._logger.info('Init runner')

    def run(self):
        while True:
            if self._cc.can_update():
                self._printer.compiling()
                make_st, curr_out = self._make()

                if make_st and self._generate_asm:
                    objdump_st, out = self._objdump()
                    if objdump_st:
                        curr_out = out

                self._printer.print_msg(make_st, curr_out)

            time.sleep(1)

def cmd_args():
    parser = ap.ArgumentParser()
    parser.add_argument('-d', '--project-dir', required=True, help='Project home dir')
    parser.add_argument('-b', '--build-dir', required=False, default='', help='Dir with makefiles')
    parser.add_argument('-a', '--asm', required=False, default=None, help='generate asm for file')

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
