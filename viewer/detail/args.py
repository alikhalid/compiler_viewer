#!/usr/bin/python

from enum import Enum
import argparse as ap
import os
import json

class Mode(Enum):
    DEVELOPER = "developer"
    INTERACTIVE = "interactive"

    @staticmethod
    def from_str(label):
        if label.lower() in ['i', 'interactive']:
            return INTERACTIVE
        elif label.lower() in ['d', 'developer']:
            return DEVELOPER
        else:
            assert False, 'Bad enum label'


DEVELOPER=Mode.DEVELOPER
INTERACTIVE=Mode.INTERACTIVE


def create_cfg(args):
    with open(args['config'], 'w') as f:
        f.write(json.dumps(args, indent=4, sort_keys=True))


def load_cfg(fname):
    args = {}
    with open(fname, 'r') as f:
        args = json.loads(f.read())

    return args


def assert_dir(path):
    assert os.path.isdir(path), 'File does not exist ' + path


def process_developer(args_in):
    args = vars(args_in)

    args['mode'] = 'DEVELOPER'
    args['watch_dirs'] = [args['project_dir']]
    args['cache_directory'] = 'viewer/__viewer_cache__'
    args['out_txt'] = 'viewer/__viewer_cache__/out.txt'
    args['cmp_exp'] = 'viewer/__viewer_cache__/cmp_exp'
    args['objdump_flags'] = ['-{}'.format(f) for f in args['objdump_flags']]
    args['build_flags'] = ['-{}'.format(f) for f in args['build_flags']]

    if not os.path.isdir(args['build_dir']):
        args['build_dir'] = os.path.join(
            args['project_dir'], args['build_dir'])


    if args['config']:
        if os.path.isfile(args['config']):
            args = load_cfg(args['config'])
        else:
            create_cfg(args)

    assert_dir(args['build_dir'])
    assert_dir(args['project_dir'])

    return args


def process_interactive(args_in):
    args = vars(args_in)

    args['mode'] = 'INTERACTIVE'
    args['executable'] = 'a.out'
    args['example_cpp'] = 'example.cpp'
    args['cache_directory'] = 'viewer/__viewer_cache__'
    args['out_txt'] = 'viewer/__viewer_cache__/out.txt'
    args['cmp_exp'] = 'viewer/__viewer_cache__/cmp_exp'
    args['project_dir'] = 'viewer/__viewer_cache__'
    args['build_dir'] = 'viewer/__viewer_cache__'
    args['watch_dirs'] = [args['project_dir']]
    args['watch_dirs'].extend(args['include_dir'])
    args['objdump_flags'] = ['-{}'.format(f) for f in args['objdump_flags']]
    args['build_flags'] = ['-{}'.format(f) for f in args['build_flags']]

    assert_dir(args['build_dir'])
    assert_dir(args['project_dir'])

    return args


def cmd_args():
    parser = ap.ArgumentParser('Compiler viewer')
    subparser = parser.add_subparsers(title='Modes', help='Mode to run in', dest='MODE')
    subparser.required = True
    parser.add_argument(
        '-a',
        '--asm',
        action='store_true',
        required=False,
        default=False,
        help='generate asm for file')
    parser.add_argument(
        '-d',
        '--disable-parsing',
        action='store_true',
        required=False,
        default=False,
        help='Disable parsing of objdump and errors')
    parser.add_argument(
        '-o',
        '--objdump-flags',
        nargs='*',
        default=[],
        help='flags for objdump without "-"')
    parser.add_argument(
        '-f',
        '--build-flags',
        required=False,
        nargs='*',
        default=[],
        help='flags for build without "-"')

    parser_interactive = subparser.add_parser('interactive', aliases=['i'], help='Interactive mode')
    parser_interactive.add_argument(
        '-i',
        '--include-dir',
        type=list,
        required=False,
        nargs='*',
        default=[],
        help='Include dir for interactive mode')

    parser_developer = subparser.add_parser('developer', aliases=['d'], help='Developer mode')
    parser_developer.add_argument(
        '-c',
        '--config',
        type=str,
        required=False,
        default='',
        help='create config if file doesnt exist else load config in json')
    parser_developer.add_argument(
        '-e',
        '--executable',
        required=False,
        default='',
        help='Executable file')
    parser_developer.add_argument(
        '-p',
        '--project-dir',
        type=str,
        required=True,
        default='',
        help='Project home dir')
    parser_developer.add_argument(
        '-b',
        '--build-dir',
        type=str,
        required=True,
        default='',
        help='Dir with makefiles')

    args = parser.parse_args()
    if Mode.from_str(args.MODE) == DEVELOPER:
        return process_developer(args)
    elif Mode.from_str(args.MODE) == INTERACTIVE:
        return process_interactive(args)
    else:
        assert False, 'Bad input'
