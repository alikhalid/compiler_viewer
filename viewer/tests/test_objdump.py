#!/usr/bin/python

from test_detail import *
from viewer.detail.build import *
from viewer.detail.objdump import *


class TestObjdump(unittest.TestCase):

    def test_objdump(self):
        args = get_mock_args_passing()
        b = Build(args)
        build_status, _ = b()
        self.assertTrue(build_status)

        od = Objdump(args)
        od_status, asm = od()
        self.assertTrue(od_status)
        self.assertTrue(len(asm) > 0)


if __name__ == '__main__':
    init_mock_logger()
    unittest.main()
