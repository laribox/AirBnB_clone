#!/usr/bin/python3

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_costum_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_quit_exits(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
