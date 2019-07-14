#!/usr/bin/python

from logger import *

import re


class parse_error:
    def __init__(self, args):
        self._disable = args['disable_parsing']
        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Init parse_error')

    def _parse_error_str(self, err_str):
        pattern = r'(.*):(\d+):(\d+):\s+error:(.*)$'
        m = re.match(pattern, err_str)
        return '\n\nIn file   : {0}\nOn line   : {1}\nerror     :{2}'.format(
            m.group(1), m.group(3), m.group(4))
        # return '\n\nIn file   : {0}\nOn line   : {1}\nOn column : {2}\nerror
        # :{3}'.format(m.group(1), m.group(2), m.group(3), m.group(4))

    def __call__(self, err_strs):
        if (self._disable):
            return asm_strs

        self._logger.info('Running parse_error')

        parsed_strs = ''
        err_pattern = r'.*error:.*'
        err_line_pattern = r'\s'
        error_on_line = False
        for line in err_strs.split('\n'):
            if re.match(err_pattern, line):
                error_on_line = True
                parsed_strs += self._parse_error_str(line)
            elif error_on_line and re.match(err_line_pattern, line):
                parsed_strs += '\n{}'.format(line)
            else:
                error_on_line = False

        return parsed_strs
