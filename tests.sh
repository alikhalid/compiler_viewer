#!/bin/sh

if [ -z $1 ]
then
    python3 -m unittest discover -s viewer/tests -p test*.py
else
    python3 -m unittest discover -s viewer/tests -p test*$1*.py
fi
