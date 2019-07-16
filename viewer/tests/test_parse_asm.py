#!/usr/bin/python

from test_detail import *
from viewer.detail.build import *
from viewer.detail.objdump import *
from viewer.detail.parse_asm import *


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

        pa = ParseAsm(args)
        parsed_asm = pa(asm)
        self.assertTrue(len(parsed_asm) > 0)
        self.assertNotEqual(asm, parsed_asm)

        args['disable_parsing'] = True
        pa = ParseAsm(args)
        parsed_asm = pa(asm)
        self.assertTrue(len(parsed_asm) > 0)
        self.assertEqual(asm, parsed_asm)


if __name__ == '__main__':
    init_mock_logger()
    unittest.main()
