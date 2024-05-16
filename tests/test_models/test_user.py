#!/usr/bin/python3

import unittest
from models.user import User


class TestUserClass(unittest.TestCase):

     def test_create_instance(self):
         obj = User()
         self.assertEqual(User, type(obj))



if __name__ == "__main__":
    unittest.main()
