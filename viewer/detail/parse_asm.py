#!/usr/bin/python

from logger import *

import re


class parse_asm:
    def __init__(self, args):
        self._disable = args['disable_parsing']
        self._logger = get_logger()
        self._log_info()

    def _log_info(self):
        self._logger.info('Init parse_asm')

    def _clean_str(self, asm_str):
        comment_pattern = r'(.*)\s*#.*$'
        hex_pattern = r'\s+[0-9a-f]+:'
        mc = re.match(comment_pattern, asm_str)
        comment_removed = mc.group(1) if mc else asm_str
        mh = re.match(hex_pattern, comment_removed)
        hex_removed = comment_removed[50:].lstrip() if mh else comment_removed
        return hex_removed

    def _fix_indent_and_add_newline(self, asm_str):
        pattern_ignore = r'^.*\(.*\).*$'
        asm_str_fixed = asm_str
        if not re.match(pattern_ignore, asm_str):
            asm_str_fixed = '\t{}'.format(asm_str)
        return '\n{}'.format(asm_str_fixed)

    def _remove_extra_newlines(self, asm_parsed):
        return re.sub(r'\n\s*\n', '\n\n', asm_parsed)

    def __call__(self, asm_strs):
        if (self._disable):
            return asm_strs

        self._logger.info('Running parse_asm')

        parsed_strs = ''
        pattern = r'.*<.*>:|Disassembly.*:$|.*:\s+file\s+format.*$'
        for line in asm_strs.split('\n'):
            if not re.match(pattern, line):
                parsed_strs += self._fix_indent_and_add_newline(
                    self._clean_str(line))

        return self._remove_extra_newlines(parsed_strs).rstrip()
