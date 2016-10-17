#!/usr/bin/env python

import sqlite3
import os
import re
import xml.etree.ElementTree as ET

class DB(object):

    """docstring for DB."""

    def __init__(self, name):
        self.name = name + ".sqlite3"
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
            print('Commit Sucessful')
            return self.conn.commit();
        except Exception as e:
            raise

    def createTable(self, tableName, tableColumns):
        if isinstance(tableName, str) and isinstance(tableColumns, dict):
            tableColumns = str(tableColumns)
            for symbol in ["'",':', ',', '{', '}']:
                if symbol in tableColumns:
                    tableColumns = tableColumns.replace(symbol, "")
            query = "CREATE TABLE IF NOT EXISTS %s (%s)" % (tableName, tableColumns)
            try:
                print("Create Table Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise


    def dropTable(self, tableName):
        if isinstance(tableName, str):
            query = "DROP TABLE IF EXISTS %s" % tableName
            try:
                print("Drop Table Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise



    def select(self, tableName, tableColumns, tableValues):
        if isinstance(tableName, str) and isinstance(tableValues, dict):
            query = "INSERT INTO {0} ({1}) VALUES ({2});".format(tableName, tableColumns, tableValues)
            print(type(query))
            print(query)
            try:
                print("Insert Values Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise

    def createTablesByColumn(self, name, columns, depth):
        if isinstance(columns, dict) and isinstance(name, str):
            try:
                for level in range(0, int(depth)):
                    self.createTable(name + str(level), columns)
            except Exception as e:
                raise

    def insert(self, tableName, tableColumns, tableValues):
        if isinstance(tableName, str) and isinstance(tableValues, dict):
            query = "INSERT INTO {0} ({1}) VALUES ({2});".format(tableName, tableColumns, tableValues)
            print(type(query))
            print(query)
            try:
                print("Insert Values Sucessful")
                self.cur.execute(query)
            except Exception as e:
                raise

    def parseXML(self, tag, columnsName, path):
        if isinstance(tag, str) and isinstance(path, str):
            try:
                context = ET.iterparse(path, events=('end',))
                for event, elem in context:
                    if re.sub('{.*?}', '', elem.tag) == tag:
                        values = []
                        level = int()
                        for item in elem:
                            values.append(item.text)
                            if re.sub('{.*?}', '', item.tag) == 'CategoryLevel':
                                level = int(item.text)
                        values = ''.join(values)
                        tableName = 'CategoryLevel' + str(level)
                        self.insert(tableName, columnsName, values)
                        values = []
                        elem.clear()
            except Exception as e:
                raise
