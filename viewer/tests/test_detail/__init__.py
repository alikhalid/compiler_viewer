#!/usr/bin/python

from .mock_args import *
import unittest
import sys
import logging


def init_mock_logger():
    logging.basicConfig(
        filename='viewer/tests/test_data/event.log',
        filemode='w',
        format='%(asctime)s %(message)s')


def close_mock_logger():
    l = logging.get_logger()
    l.close()
