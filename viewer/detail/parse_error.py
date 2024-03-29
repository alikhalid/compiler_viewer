#!/usr/bin/python

from .logger import *

import re


class ParseError:
    def __init__(self, args):
        """
        Parses the compiler error and returns a cleaned
        more redable version of it
        """
        self.__disable = args['disable_parsing']
        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        """Log basic info"""
        self.__logger.info('Init ParseError')

    def __parse_error_str(self, err_str):
        """
        Parses the error string based on pattern.
        Extracts file name, line no and the error message
        """
        pattern = r'(.*):(\d+):(\d+):\s+error:(.*)$'
        m = re.match(pattern, err_str)
        return '\n\nIn file   : {0}\nOn line   : {1}\nerror     :{2}'.format(
            m.group(1), m.group(3), m.group(4))
        # return '\n\nIn file   : {0}\nOn line   : {1}\nOn column : {2}\nerror
        # :{3}'.format(m.group(1), m.group(2), m.group(3), m.group(4))

    def __call__(self, err_strs):
        """
        Goes through every line of the output and looks for
        the error parrern, if found parses it and adds it to a
        list. Lines following the error messages that are
        indented contain information about the error so we keep
        those as well
        """
        if (self.__disable):
            return err_strs

        self.__logger.info('Running ParseError')

        parsed_strs = ''
        err_pattern = r'.*error:.*'
        err_line_pattern = r'\s'
        error_on_line = False
        for line in err_strs.split('\n'):
            if re.match(err_pattern, line):
                error_on_line = True
                parsed_strs += self.__parse_error_str(line)
            elif error_on_line and re.match(err_line_pattern, line):
                parsed_strs += '\n{}'.format(line)
            else:
                error_on_line = False

        return parsed_strs
