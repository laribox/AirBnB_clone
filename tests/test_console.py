#!/usr/bin/python3

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_costum_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)
        
        
