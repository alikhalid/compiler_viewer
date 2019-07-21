#!/usr/bin/python

def get_mock_args_passing():
    args = {}

    args['asm'] = True
    args['executable'] = 'a.out'
    args['example_cpp'] = 'example.cpp'
    args['project_dir'] = 'viewer/tests/test_data/psssing'
    args['watch_dirs'] = [args['project_dir']]
    args['build_dir'] = 'viewer/tests/test_data/passing'
    args['include_dir'] = None
    args['objdump_flags'] = []
    args['build_flags'] = ["-std=c++17", "-O3"]
    args['disable_parsing'] = False

    return args


def get_mock_args_failing():
    args = {}

    args['asm'] = True
    args['executable'] = 'a.out'
    args['example_cpp'] = 'example.cpp'
    args['project_dir'] = 'viewer/tests/test_data/failing'
    args['watch_dirs'] = [args['project_dir']]
    args['build_dir'] = 'viewer/tests/test_data/failing'
    args['include_dir'] = None
    args['objdump_flags'] = []
    args['build_flags'] = ["-std=c++17", "-O3"]
    args['disable_parsing'] = False

    return args

def get_mock_args_passing_a_out():
    args = {}

    args['asm'] = True
    args['executable'] = 'a.out'
    args['example_cpp'] = 'example.cpp'
    args['build_dir'] = 'viewer/tests/test_data/passing_a_out'
    args['out_txt'] = 'viewer/tests/test_data/passing_a_out/out.txt'
    args['build_flags'] = ["-std=c++17", "-O3"]
    args['include_dir'] = None

    return args


def get_mock_args_failing_a_out():
    args = {}

    args['asm'] = True
    args['executable'] = 'a.out'
    args['example_cpp'] = 'example.cpp'
    args['build_dir'] = 'viewer/tests/test_data/failing_a_out'
    args['out_txt'] = 'viewer/tests/test_data/failing_a_out/out.txt'
    args['build_flags'] = ["-std=c++17", "-O3"]
    args['include_dir'] = None

    return args
