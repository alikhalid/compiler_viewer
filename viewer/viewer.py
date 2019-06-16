#!/usr/bin/python

from detail import *
import argparse as ap
import os, time

class runner:
    def __init__(self, args):
        self._project_dir = args['project_dir']
        self._fname = os.path.join(os.getcwd(), '__viewer_cache__/cmp_exp')

        self._cc = check_changes(args)
        self._make = make(args)
        self._objdump = objdump(args)

        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Starting runner')
        self._logger.info('Project dir: {}'.format(self._project_dir))

    def _print_msg(self, success, msg=""):
        if success:
            self._logger.info('Compilation successful')
            write_to_file(self._fname, "Compilation successful!\n{0}".format(msg))
        else:
            self._logger.info('Compilation failed')
            write_to_file(self._fname, "Compilation failed!\n{0}".format(msg))

    def run(self):
        while True:
            if self._cc.can_update():
                if self._cc.can_reset():
                    self._cc.reset()
                write_to_file(self._fname, 'Compiling...')
                passed, curr_out = self._make()
                if passed:
                    obj_st, out = self._objdump()
                    if obj_st:
                        curr_out = out
                self._print_msg(passed, curr_out)

            time.sleep(1)

    def reset(self):
        self._logger.info('Resetting runner')
        os.remove(self._fname)

def cmd_args():
    parser = ap.ArgumentParser()
    parser.add_argument('-d', '--project-dir', required=False, default=os.getcwd(), help='Project home dir')
    parser.add_argument('-b', '--build-dir', required=False, default='build', help='Dir with makefiles')
    parser.add_argument('-j', required=False, default=1, help='-j option for make command')
    parser.add_argument('-a', '--asm', required=False, default=False, action='store_true', help='generate asm')
    parser.add_argument('-o', '--obj-file', required=False, default=1, help='obj filename used with asm')

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
