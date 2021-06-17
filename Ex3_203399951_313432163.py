#!/usr/bin/python

# import unittest
import csv
import sys
import pytesseract

path_to_csv = ''
table = []


# class TesseractTest(unittest.TestCase):
def setUp():
    with open(path_to_csv, 'r') as data:
        for line in csv.DictReader(data):
            table.append(line)


def test():
    # self.setUpClass()
    for line in table:
        print(pytesseract.image_to_string(line['Path'] + line['Filename']))
    # self.assertEqual(1, 1)


# def test_isupper(self):
#     self.assertTrue('FOO'.isupper())
#     self.assertFalse('Foo'.isupper())
#
# def test_split(self):
#     s = 'hello world'
#     self.assertEqual(s.split(), ['hello', 'world'])
#     # check that s.split fails when the separator is not a string
#     with self.assertRaises(TypeError):
#         s.split(2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("please enter one arg with csv file path")
    path_to_csv = sys.argv[1]
    setUp()
    test()
