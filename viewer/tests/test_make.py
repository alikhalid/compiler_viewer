#!/usr/bin/python

from test_detail import *
from viewer.detail.make import *


class TestBuild(unittest.TestCase):

    def test_passing_build(self):
        args = get_mock_args_passing_make()
        m = Make(args)
        status, msg = m()
        self.assertTrue(status)


if __name__ == '__main__':
    init_mock_logger()
    unittest.main()
    close_mock_logger()
