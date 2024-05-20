#!/usr/bin/python3

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
 

class TestHBNBCommand(unittest.TestCase):

    __list = ["User", "City", "Place, BaseModel",
              "State", "Amenity", "Review"]

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

    def test_help_quit(self):
        txt = "Quits console"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(txt, output.getvalue().strip())

    def test_help_EOF(self):
        txt = "Exits console"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(txt, output.getvalue().strip())

    def test_help_create(self):
        txt = ("Create a new instance of a class.\n        "
               "Usage: create <class_name>")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual(txt, output.getvalue().strip()) 

    def test_create_missing_class(self):
        errorString = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(errorString, output.getvalue().strip())

    def test_create_invalid_class(self):
        errorString = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(errorString, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            Key = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            Key = f"User.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            Key = f"State.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            Key = f"City.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            Key = f"Amenity.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            Key = f"Place.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            Key = f"Review.{output.getvalue().strip()}"
            self.assertIn(Key, storage.all().keys())

    def test_show(self):
        for item in self.__list:
            with patch ('sys.stdout', new=StringIO()) as output:
                HBNBCommand().onecmd("create " + item)
                uid = output.getvalue().strip()
                key = item + "." + uid
                self.assertIn(key, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
