#!/usr/bin/python

import os

class Skeleton:
    def __init__(self):
        self.__fname = 'viewer/__viewer_cache__/example.cpp'

    def __call__(self):
        if not os.path.isfile(self.__fname):
            with open(self.__fname, 'w') as f:
                f.write(self.__main_skeleton())

    def __main_skeleton(self):
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
    s = Skeleton()
    s()
