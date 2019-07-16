#!/usr/bin/python

def get_mock_args_passing():
    args = {}

    args['mode'] = 'INTERACTIVE'
    args['asm'] = 'a.out'
    args['project_dir'] = 'viewer/tests/test_data/psssing'
    args['watch_dirs'] = [args['project_dir']]
    args['build_dir'] = 'viewer/tests/test_data/passing'
    args['include_dir'] = None
    args['objdump_flags'] = []
    args['build_flags'] = ["-std=c++17", "-O3"]

    return args


def get_mock_args_failing():
    args = {}

    args['mode'] = 'INTERACTIVE'
    args['asm'] = 'a.out'
    args['project_dir'] = 'viewer/tests/test_data/failing'
    args['watch_dirs'] = [args['project_dir']]
    args['build_dir'] = 'viewer/tests/test_data/failing'
    args['include_dir'] = None
    args['objdump_flags'] = []
    args['build_flags'] = ["-std=c++17", "-O3"]
    args['disable_parsing'] = False

    return args
