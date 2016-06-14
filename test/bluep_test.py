import unittest
import sys
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from back.console import Console


class BluePTest(unittest.TestCase):

    def test_console(self):
        console = Console(sys.stdout, sys.stderr, './')
        self.assertNotEqual(console, None)

        console.eval_command("TEST_VAR=\"TEST_VALUE\"")
        print_result = console.eval_command("print(TEST_VAR)")
        self.assertEqual("TEST_VALUE\n", print_result)

        console.eval_command("from front.edge import Edge")
        console.eval_command("test_edge = Edge(None, None)")

        console.refresh_instance_list()
        self.assertEqual(True, "Edge" in console.instances)

        console.flush_console()
        self.assertEqual(False, "Edge" in console.instances)

if __name__ == '__main__':
    unittest.main()
