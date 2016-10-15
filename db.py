#!/usr/bin/env python

import sqlite3

class DB(object):

    """docstring for DB."""

    def __init__(self, name):
        self.name = name
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.name)
            self.cur = self.conn.cursor();
        except Exception as e:
            print(e)
            raise

    def __del__(self):
        try
            return self.conn.close()
        except Exception as e:
            print(e)
            raise Exception(query + " Error Not Close")

    def drop(self):
        try:
            ## Delete File
        except Exception as e:
            print(e)
            raise Exception(" Error File Not Found")

    def commit(self):
        try:
            return self.conn.commit();
        except Exception as e:
            raise

    def query(self, name, query, values):
        queries = {
          'create': self.conn.execute("CREATE TABLE {0};".format(self.name),
          'insert': self.conn.execute("INSERT INTO {0} VALUES {1}").format(self.name, values),
          'drop': self.conn.execute("DROP TABLE " + self.name + ";")
        }[value](x)
        try:
            return self.conn.execute(queries[query])
        except Exception as e:
            raise
