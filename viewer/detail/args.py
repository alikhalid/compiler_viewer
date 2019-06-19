#!/usr/bin/python

import argparse as ap
import os, json

def cmd_args():
    parser = ap.ArgumentParser('Compiler viewer')
    parser.add_argument('-m', '--mode', required=True, default='i', help='Interactive or developer mode')
    parser.add_argument('-p', '--project-dir', help='Project home dir')
    parser.add_argument('-i', '--include-dir', nargs='*', default=[], help='Include dir for interactive mode')
    parser.add_argument('-b', '--build-dir', required=False, default='', help='Dir with makefiles')
    parser.add_argument('-a', '--asm', nargs='*', required=False, default=None, help='generate asm for file')
    parser.add_argument('-f', '--flags', nargs='*', required=False, default=[], help='flags for gcc without "-"')

    args = vars(parser.parse_args())

    if args['mode'].lower() in ['i', 'interactive']:
        args['mode'] = 'INTERACTIVE'
        if args['asm'] != None:
            args['asm'] = 'a.out'

        args['project_dir'] = '__viewer_cache__'
        args['watch_dirs'] = [args['project_dir']]
        args['watch_dirs'].extend(args['include_dir'])
        args['flags'] = ['-{}'.format(f) for f in args['flags']]

    elif args['mode'].lower() in ['d', 'developer']:
        args['mode'] = 'DEVELOPER'
        if args['asm'] != None:
            if len(args['asm']) > 0:
                args['asm'] = args['asm'][0]
            else:
                args['asm'] = None
        args['watch_dirs'] = [args['project_dir']]
    else:
        assert False, 'Unknown mode'

    args['build_dir'] = os.path.join(args['project_dir'], args['build_dir'])

    return args
