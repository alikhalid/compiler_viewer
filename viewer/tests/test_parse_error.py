#!/usr/bin/python

from test_detail import *
from viewer.detail.build import *
from viewer.detail.parse_error import *


class TestParseError(unittest.TestCase):

    def test_parse_error(self):
        args = get_mock_args_failing()
        b = Build(args)
        status, msg = b()
        self.assertTrue(len(msg) > 0)
        self.assertFalse(status)

        pe = ParseError(args)
        parsed_msg = pe(msg)
        self.assertNotEqual(parsed_msg, msg)

        args['disable_parsing'] = True
        pe = ParseError(args)
        parsed_msg = pe(msg)
        self.assertEqual(parsed_msg, msg)


if __name__ == '__main__':
    init_mock_logger()
    unittest.main()
