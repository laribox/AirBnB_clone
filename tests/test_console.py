#!/usr/bin/python3

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def test_costum_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_quit_exits(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
