#!/bin/sh

if [ -z $1 ]
then
    python -m unittest discover -s viewer/tests -p test*.py
else
    python -m unittest discover -s viewer/tests -p test*$1*.py
fi
