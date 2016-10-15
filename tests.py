#!/usr/bin/env python

import unittest
import db

class TestDBMethods(unittest.TestCase):

def testDB(self):
    self.assertEqual('foo'.upper(), 'FOO')
