#!/usr/bin/python

from test_detail import *
from viewer.detail.build import *


class TestBuild(unittest.TestCase):

    def test_passing_build(self):
        args = get_mock_args_passing()
        b = Build(args)
        status, _ = b()
        self.assertTrue(status)

    def test_passing_build(self):
        args = get_mock_args_failing()
        b = Build(args)
        status, msg = b()
        self.assertTrue(len(msg) > 0)
        self.assertFalse(status)


if __name__ == '__main__':
    init_mock_logger()
    unittest.main()
    close_mock_logger()

