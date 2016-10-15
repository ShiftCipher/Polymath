#!/usr/bin/env python

import sqlite3
import os

class DB(object):

    """docstring for DB."""

    def __init__(self, name):
        name = name + ".sqlite"
        self.name = name
        self.conn = None
        self.cur = None
        self.create()

    def create(self):
        if os.path.isfile(self.name):
            print("File %s Exist" % self.name)
            pass
        else:
            try:
                file = open(self.name, "w+")
                print("Creating %s" % self.name)
            except Exception as e:
                raise

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.name)
            self.cur = self.conn.cursor()
            print("Connecting to %s" % self.name)
            return self.cur
        except Exception as e:
            raise

    def close(self):
        try:
            if self.conn != None:
                print("Closing Conection Manually")
                return self.conn.close()
            else:
                print("Please Connect the Database")
        except Exception as e:
            raise

    def __del__(self):
        try:
            if self.conn != None:
                print("Secure Conection Close by Object Deletion or Program End")
                return self.conn.close()
            else:
                print("The Database is Closed Now")
        except Exception as e:
            raise

    def drop(self):
        try:
            if os.path.isfile(self.name):
                os.remove(self.name)
                print("Sucessful Delete Filename %s" % self.name)
        except Exception as e:
            raise

    def commit(self):
        try:
            return self.cur.commit();
        except Exception as e:
            raise

    def createTable(self, tableName, tableFields):
        if type(tableName) is str and type(tableFields) is dict:
            query = "CREATE TABLE %s %s" % (tableName, for x in tableFields : x + ' ' + x[value])
            try:
                print("Create Table Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise

    def dropTable(self, tableName):
        if type(tableName) is str:
            query = "DROP TABLE %s" % tableName
            try:
                print("Drop Table Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise

    def insertTable(self, tableName, tableFieldsValues):
        if type(tableName) is str and type(tableFieldsValues) is dict:
            query = "INSERT INTO %s VALUES %s" % (tableName, tableFieldsValues)
            try:
                print("Insert Values Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise
        else:
            raise Exception("Query Must Be String")

ebay = DB('ebay')
ebay.connect()

fields = {
    'BestOfferEnabled' : 'boolean',
    'AutoPayEnable' : 'boolean',
    'CategoryID' : 'integer',
    'CategoryName' : 'string',
    'CategoryParentID' : 'integer'
}

ebay.createTable('daniel', fields)
ebay.close()
ebay.drop()
