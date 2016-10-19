#!/usr/bin/env python

import sqlite3
import os
import re
import xml.etree.ElementTree as ET
import itertools

class Table(object):

    """docstring for Table."""

    def __init__(self, name):
        self.columns = {}
        self.arg = name

    def addColumn(self, name, value):
        self.columns[name] = value

    def getAllColumns(self):
        return self.columns

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
        print('Trying to Connect to Database')
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
                print("Secure Conection Close")
                return self.conn.close()
            else:
                print("Please Connect the Database")
        except Exception as e:
            raise

    def __del__(self):
        try:
            if self.conn != None:
                print("Secure Conection by Terminate Script")
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

    def getAllTables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';");
        data = self.cur.fetchone()
        return data

    def getTableInfo(self, table):
        self.cur.execute("SELECT * FROM %s;" % table);
        data = self.cur.fetchall()
        return data

    def dropTable(self, tableName):
        if isinstance(tableName, str):
            query = "DROP TABLE IF EXISTS %s" % tableName
            try:
                print("Drop Table Sucessful")
                return self.cur.execute(query)
            except Exception as e:
                raise

    def selectOneId(self, tableName, CategoryID):
        if isinstance(tableName, str) and isinstance(CategoryID, str):
            try:
                query = """
                SELECT CategoryID, CategoryParentID, CategoryLevel, CategoryName, BestOfferEnabled
                FROM ({0})
                WHERE CategoryID = {1};""".format(tableName, CategoryID)
                self.cur.execute(query)
                data = self.cur.fetchone()
                if not data:
                    pass
                elif data == None:
                    pass
                else:
                    return data
            except Exception as e:
                raise

    def selectAllId(self, tableName, CategoryID):
        if isinstance(tableName, str) and isinstance(CategoryID, str):
            try:
                query = """
                SELECT CategoryID, CategoryParentID, CategoryLevel, CategoryName, BestOfferEnabled
                FROM ({0}) WHERE CategoryID = {1};""".format(tableName, CategoryID)
                self.cur.execute(query)
                data = self.cur.fetchall()
                if not data:
                    pass
                elif data == None:
                    pass
                else:
                    return data
            except Exception as e:
                raise

    def selectIdbyParent(self, tableName, CategoryParentID):
        if isinstance(tableName, str) and isinstance(CategoryParentID, str):
            try:
                query = """
                SELECT CategoryID, CategoryParentID, CategoryLevel, CategoryName, BestOfferEnabled
                FROM ({0}) WHERE CategoryParentID = {1};""".format(tableName, CategoryParentID)
                self.cur.execute(query)
                data = self.cur.fetchall()
                return data
            except Exception as e:
                raise

    def bulkCreate(self):
        tableName = 'CategoryLevel'
        table = Table(tableName)
        level = 0
        table.addColumn('BestOfferEnabled', 'text')
        table.addColumn('AutoPayEnabled', 'text')
        table.addColumn('CategoryID', 'text not null')
        table.addColumn('CategoryLevel', 'text')
        table.addColumn('CategoryName', 'text')
        table.addColumn('BestOfferEnabled', 'text')
        table.addColumn('CategoryParentID', 'text')
        table.addColumn('LeafCategory', 'text')
        table.addColumn('LSD', 'text')
        tableColumns = table.getAllColumns()
        tableColumns = str(tableColumns)

        for symbol in ["'", ':', '{', '}']:
            if symbol in tableColumns:
                tableColumns = tableColumns.replace(symbol, "")

        for level in range(0, int(6)):
            level += 1
            query = "CREATE TABLE IF NOT EXISTS {0} ({1})".format(tableName + str(level), tableColumns)
            print(query)
            self.conn.execute(query)

    def bulkInsert(self, tag, path):
        if isinstance(tag, str) and isinstance(path, str):
            try:
                itertree = ET.iterparse(path)
                total = 0
                for event, elem in itertree:
                    if re.sub('{.*?}', '', elem.tag) == tag:
                        row = {}
                        columns = []
                        values = []
                        categoryLevel = 0
                        for item in elem:
                            value = item.text.replace('\'', "")
                            value = "'%s'" % value
                            column = re.sub('{.*?}', '', item.tag)
                            values.append(value)
                            columns.append(column)
                            if column == 'CategoryLevel':
                                categoryLevel = int(item.text)
                        elem.clear()
                        columns = ", ".join(columns)
                        values = ", ".join(values)
                        total += 1
                        query = 'INSERT INTO {0} ({1}) VALUES ({2})'.format('CategoryLevel' + str(categoryLevel), columns, values)
                        print(query)
                        self.cur.execute(query)
                print('Total Records Insert %s' % str(total))
            except Exception as e:
                raise
