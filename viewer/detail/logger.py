#!/usr/bin/python

import logging

def init_logger():
    logging.basicConfig(filename='viewer/__viewer_cache__/event.log', filemode='w', format='%(asctime)s %(message)s')

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger
