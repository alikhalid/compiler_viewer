#!/usr/bin/python

from detail import *
import os, time, sys

class i_runner:
    def __init__(self, args):
        self._logger = get_logger()
        self._log_info()

        self._printer = printer()
        self._cc = check_changes(args)
        self._build = build(args)

        self._generate_asm = args['asm']
        if self._generate_asm:
            self._objdump = objdump(args)

    def _log_info(self):
        self._logger.info('Init i_runner')

    def run(self):
        while True:
            if self._cc.can_update():
                self._printer.compiling()
                make_st, curr_out = self._build()

                if make_st and self._generate_asm:
                    objdump_st, out = self._objdump()
                    if objdump_st:
                        curr_out = out

                self._printer.print_msg(make_st, curr_out)

            time.sleep(1)

class d_runner:
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
        self._logger.info('Init d_runner')

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

def get_runner(args):
    if args['mode'] == 'INTERACTIVE':
        return i_runner(args)
    elif args['mode'] == 'DEVELOPER':
        return d_runner(args)

def main():
    args = cmd_args()
    init_logger()

    logger = get_logger()
    logger.info(args)
    logger.info('Starting compiler viewer')
    logger.info('running from dir: {}'.format(os.getcwd()))

    while True:
        r = get_runner(args)
        try:
            r.run()
        except KeyboardInterrupt:
            logger.info("Exiting now")
            sys.exit(0)
        except Exception as e:
            logger.info('Caught exception: {0}'.format(str(e.message)))

if __name__ == '__main__':
    main()
