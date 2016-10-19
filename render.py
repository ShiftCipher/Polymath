#!/usr/bin/env python

import db

class Tree(object):
    """docstring for Root."""
    def __init__(self, tableName, categoryId):
        self.tableName = tableName
        self.categoryId = str(categoryId)
        self.lvl = int()
        self.found = False
        self.node = None
        self.file = None
        self.steps = 6 - self.lvl

    def getTree(self, DB):
        for level in range(1, 7):
            node = DB.selectOneId(self.tableName + str(level), self.categoryId)
            if node != None:
                self.node = [node]
                self.lvl = int(node[2])
                self.found = True

        if self.node != None:
            node = self.node[0]
            print("*" * 15 + " CategoryID Found %s" % str(self.lvl) + " " + "*" * 15)
            self.file.write("<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))

            for value in range(1, self.steps):
                if self.lvl > 1:
                    nodes = DB.selectOneId(self.tableName + str(self.lvl - 1), node[1])
                    self.file.write("<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                else:
                    nodes = DB.selectOneId(self.tableName + str(self.lvl), node[1])
                    self.file.write("<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
            self.file.write("</div>\n")

            self.getLeafNodes(self.node, DB)
            self.file.write("</div>\n")

        if self.found == False:
            print("*" * 15 + " CategoryID Not Found" + " " + "*" * 15)
            sys.exit("*" * 15 + " Terminate Script" + " " + "*" * 15)


    def getLeafNodes(self, nodes, DB):
        level = self.lvl
        while(level < 7):
            leafs = []
            level += 1
            for node in nodes:
                self.file.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                value = node[0]
                if level < 7:
                    leafs = DB.selectIdbyParent(self.tableName + str(level), value)
                    self.getLeafNodes(leafs, DB)
            self.file.write("\t" * level + "</div>\n")

    def Tree2HTML(self):
        ebayDB = db.DB('ebay')
        ebayDB.connect()
        self.file = open("html/" + self.categoryId + ".html" , "w+")
        self.getTree(ebayDB)
        self.file.close()
        ebayDB.close()
