#!/usr/bin/python

from .logger import *
import re


class ParseAsm:
    def __init__(self, args):
        self.__disable = args['disable_parsing']
        self.__logger = get_logger()
        self.__log_info()

    def __log_info(self):
        self.__logger.info('Init ParseAsm')

    def __clean_str(self, asm_str):
        comment_pattern = r'(.*)\s*#.*$'
        hex_pattern = r'\s+[0-9a-f]+:'
        mc = re.match(comment_pattern, asm_str)
        comment_removed = mc.group(1) if mc else asm_str
        mh = re.match(hex_pattern, comment_removed)
        hex_removed = comment_removed[50:].lstrip() if mh else comment_removed
        return hex_removed

    def __fix_indent_and_add_newline(self, asm_str):
        pattern_ignore = r'^.*\(.*\).*$'
        asm_str_fixed = asm_str
        if not re.match(pattern_ignore, asm_str):
            asm_str_fixed = '\t{}'.format(asm_str)
        return '\n{}'.format(asm_str_fixed)

    def __remove_extra_newlines(self, asm_parsed):
        return re.sub(r'\n\s*\n', '\n\n', asm_parsed)

    def __call__(self, asm_strs):
        if (self.__disable):
            return asm_strs

        self.__logger.info('Running ParseAsm')

        parsed_strs = ''
        pattern = r'.*<.*>:|Disassembly.*:$|.*:\s+file\s+format.*$'
        for line in asm_strs.split('\n'):
            if not re.match(pattern, line):
                parsed_strs += self.__fix_indent_and_add_newline(
                    self.__clean_str(line))

        return self.__remove_extra_newlines(parsed_strs).rstrip()
