#!/usr/bin/python

import os

class skeleton:
    def __init__(self):
        self._fname = 'viewer/__viewer_cache__/example.cpp'

    def __call__(self):
        if not os.path.isfile(self._fname):
            with open(self._fname, 'w') as f:
                f.write(self._main_skeleton())

    def _main_skeleton(self):
        return """/*
#include <iostream>
#include <string>
#include <vector>
*/

int main(){
    /* your_code_here */
    return 0;
}"""

if __name__ == '__main__':
    s = skeleton()
    s()
