#!/usr/bin/python

from test_detail import *
from viewer.detail.build import *
from viewer.detail.a_out import *


class TestAout(unittest.TestCase):

    def test_passing_a_out(self):
        args = get_mock_args_passing_a_out()
        b = Build(args)
        b()
        a_out = Aout(args)
        status = a_out()

        self.assertTrue(status)

    def test_failing_a_out(self):
        args = get_mock_args_failing_a_out()
        b = Build(args)
        b()
        a_out = Aout(args)
        status = a_out()

        self.assertFalse(status)


if __name__ == '__main__':
    init_mock_logger()
    unittest.main()
    close_mock_logger()
