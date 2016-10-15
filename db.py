#!/usr/bin/env python

import sqlite3
import os

class DB(object):

    """docstring for DB."""

    def __init__(self, name):
        name = name + ".db"
        self.name = name
        self.conn = None
        self.cur = None
        self.create()

    def create(self):
        if os.path.isfile(self.name):
            pass
        else:
            try:
                file = open(self.name, "w+")
            except Exception as e:
                print(e)
                raise

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.name)
            self.cur = self.conn.cursor();
        except Exception as e:
            print(e)
            raise

    def __del__(self):
        try:
            if self.conn != None and self.cur != None:
                print("Closing Conection by Object Deletion or Program Exit")
                return self.cur.close()
            else:
                print("Please Connect the Database")
        except Exception as e:
            print(e)
            raise

    def drop(self):
        try:
            if os.path.isfile(self.name):
                os.remove(self.name)
                print("Sucessful Delete Filename %s" % self.name)
        except Exception as e:
            print(e)
            raise

    def commit(self):
        try:
            return self.conn.commit();
        except Exception as e:
            raise

    def query(self, name, query, values):
        if type(name) is str and type(query) is str and values is str:
            if query == 'create':
                query = "CREATE TABLE %s;" % name
            elif query == 'drop':
                query = "DROP TABLE %s;" % name
            elif query == 'insert':
                query = "INSERT INTO %s VALUES %s" % self.name, values
            try:
                return self.conn.execute(query)
            except Exception as e:
                print(e)
                raise

ebay = DB('ebay')
ebay.connect()
ebay.query('', '')
ebay.drop()
