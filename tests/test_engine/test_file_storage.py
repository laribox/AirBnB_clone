#!/usr/bin/python3

import unittest

from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    
    def test_object_instance(self):
        file_storage = FileStorage()
        
    def test_type_of_filestorage_instance(self):
        self.assertEqual(type(FileStorage()), FileStorage)


class Test_FileStorage_methods(unittest.TestCase):
        
    def test_all(self):
        self.assertEqual(





if __name__ == '__main__':
    unittest.main()
