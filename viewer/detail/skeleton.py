#!/usr/bin/python

from logger import *

class skeleton:
    def __init__(self, args):
        self._fname = '__viewer_cache__/example.cpp'

        #self._logger = get_logger()
        #self._log_info()

    def _log_info(self):
        self._logger.info('Init skeleton')
        self._logger.info('\tfile naem: {}'.format(self._fname))

    def __call__(self):
        with open(self._fname, 'w') as f:
            f.write(self._main_skeleton())

    def _main_skeleton(self):
        return """/*
#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <type_traits>
*/

int main(){
    /* your_code_here */
    return 0;
}"""
