#!/usr/bin/python

from detail import *
import os
import time
import sys
import traceback


class IRunner:
    def __init__(self, args):
        self.__logger = get_logger()
        self.__log_info()

        self.__printer = Printer(args)
        self.__cc = CheckChanges(args)
        self.__build = Build(args)

        self.__generate_asm = args['asm']
        if self.__generate_asm:
            self.__objdump = Objdump(args)

    def __log_info(self):
        self.__logger.info('Init IRunner')

    def run(self):
        while True:
            if self.__cc.can_update():
                self.__printer.compiling()
                make_st, curr_out = self.__build()

                if make_st and self.__generate_asm:
                    objdump_st, out = self.__objdump()
                    if objdump_st:
                        curr_out = out

                self.__printer.print_msg(make_st, curr_out)

            time.sleep(1)


class DRunner:
    def __init__(self, args):
        self.__logger = get_logger()
        self.__log_info()

        self.__printer = Printer(args)
        self.__cc = CheckChanges(args)
        self.__make = Make(args)

        self.__generate_asm = args['asm']
        if self.__generate_asm:
            self.__objdump = Objdump(args)

    def __log_info(self):
        self.__logger.info('Init DRunner')

    def run(self):
        while True:
            if self.__cc.can_update():
                self.__printer.compiling()
                make_st, curr_out = self.__make()

                if make_st and self.__generate_asm:
                    objdump_st, out = self.__objdump()
                    if objdump_st:
                        curr_out = out

                self.__printer.print_msg(make_st, curr_out)

            time.sleep(1)


def get_runner(args):
    if args['mode'] == 'INTERACTIVE':
        return IRunner(args)
    elif args['mode'] == 'DEVELOPER':
        return DRunner(args)


def main():
    args = cmd_args()
    init_logger()

    logger = get_logger()
    logger.info(args)
    logger.info('Starting compiler viewer')
    logger.info('running from dir: {}'.format(os.getcwd()))

    trys = 10
    while True:
        r = get_runner(args)
        try:
            r.run()
        except KeyboardInterrupt:
            logger.info("Exiting now")
            sys.exit(0)
            close_logger()
        except Exception as e:
            logger.info('Caught exception: {0}'.format(str(e.message)))
            logger.error(traceback.format_exc())
            trys -= 1
            if trys == 0:
                logger.error(traceback.format_exc())
                sys.exit(1)
                close_logger()


if __name__ == '__main__':
    main()
