#!/usr/bin/python

import argparse as ap
import os, json

def create_cfg(args):
    args['config'] = args['config'] + '.json'
    with open(args['config'], 'w') as f:
        f.write(json.dumps(args, indent=4, sort_keys=True))

def load_cfg(fname):
    args = {}
    with open(fname, 'r') as f:
        args = json.loads(f.read())

    return args

def cmd_args():
    parser = ap.ArgumentParser('Compiler viewer')
    parser.add_argument('-c', '--config', required=False, type=str, default=None, help='create config if file doesnt exist else load config in json')
    parser.add_argument('-m', '--mode', required=False, default=None, help='Interactive or developer mode')
    parser.add_argument('-p', '--project-dir', help='Project home dir')
    parser.add_argument('-i', '--include-dir', nargs='*', default=[], help='Include dir for interactive mode')
    parser.add_argument('-b', '--build-dir', required=False, default='', help='Dir with makefiles')
    parser.add_argument('-a', '--asm', nargs='*', required=False, default=None, help='generate asm for file')
    parser.add_argument('-of', '--objdump-flags', nargs='*', required=False, default=[], help='flags for objdump without "-"')
    parser.add_argument('-f', '--build-flags', nargs='*', required=False, default=[], help='flags for build without "-"')

    args = vars(parser.parse_args())

    if args['config']:
        if os.path.isfile(args['config']):
            args = load_cfg(args['config'])
        else:
            create_cfg(args)

    if args['mode'].lower() in ['i', 'interactive']:
        args['mode'] = 'INTERACTIVE'
        if args['asm'] != None:
            args['asm'] = 'a.out'

        args['project_dir'] = 'viewer/__viewer_cache__'
        args['watch_dirs'] = [args['project_dir']]
        args['watch_dirs'].extend(args['include_dir'])

    elif args['mode'].lower() in ['d', 'developer']:
        args['mode'] = 'DEVELOPER'
        if args['asm'] != None:
            if len(args['asm']) > 0:
                args['asm'] = args['asm'][0]
            else:
                args['asm'] = None
        args['watch_dirs'] = [args['project_dir']]
    else:
        assert False, 'Unknown mode try either: I or D'

    if not os.path.isdir(args['build_dir']):
        args['build_dir'] = os.path.join(args['project_dir'], args['build_dir'])

    args['objdump_flags'] = ['-{}'.format(f) for f in args['objdump_flags']]
    args['build_flags'] = ['-{}'.format(f) for f in args['build_flags']]

    return args
