#!/usr/bin/env python

import db
import sys

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

    def getRootLevel(self, DB):
        for level in range(1, 7):
            node = DB.selectOneId(self.tableName + str(level), self.categoryId)
            if node != None:
                self.node = [node]
                self.lvl = int(node[2])
                self.found = True
        return self.lvl

    def getRootNodes(self, DB, html):
        node = self.node[0]
        level = self.lvl
        for value in range(1, self.steps):
            if level > 2:
                level -= 1
                nodes = DB.selectOneId(self.tableName + str(level), node[1])
                html.write("<div class=L{0}>{1} {2} {3} {4}</div>\n".format(node[2], node[0], node[3], node[2], node[4]))

    def getLeafNodes(self, nodes, DB, html):
        level = self.lvl
        while(level < 7):
            leafs = []
            level += 1
            for node in nodes:
                space = int(node[2])
                html.write("\t" * space + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                value = node[0]
                if level < 7:
                    leafs = DB.selectIdbyParent(self.tableName + str(level), value)
                    self.getLeafNodes(leafs, DB, html)
                html.write("\t" * level + "</div>\n")


    def Tree2HTML2(self):
        ebayDB = db.DB('ebay')
        ebayDB.connect()

        html = open("html/" + self.categoryId + ".html" , "w+")

        self.getRootLevel(ebayDB)
        self.getRootNodes(ebayDB, html)
        self.getLeafNodes(self.node, ebayDB, html)


    def Tree2HTML(self):
        ebayDB = db.DB('ebay')
        ebayDB.connect()

        html = open("html/" + self.categoryId + ".html" , "w+")

        self.getRootLevel(ebayDB)
        self.getRootNodes(ebayDB, html)

        found = False
        start = int()
        table = 'CategoryLevel'

        ebayDB.close()

        node = self.node[0]
        if node != None:
            html.write("<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
            value = node[0]
            nodes = ebayDB.selectIdbyParent(self.tableName + str(1), value)
            #print(nodes)

            for node in nodes:
                level = int(node[2])
                html.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                value = node[0]
                nodes = ebayDB.selectIdbyParent(self.tableName + str(2), value)
                #print(nodes)

                for node in nodes:
                    level = int(node[2])
                    html.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                    value = node[0]
                    nodes = ebayDB.selectIdbyParent(self.tableName + str(3), value)
                    #print(nodes)

                    for node in nodes:
                        level = int(node[2])
                        html.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                        value = node[0]
                        nodes = ebayDB.selectIdbyParent(self.tableName + str(4), value)
                        #print(nodes)

                        for node in nodes:
                            level = int(node[2])
                            html.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                            value = node[0]
                            nodes = ebayDB.selectIdbyParent(self.tableName + str(5), value)
                            #print(nodes)

                            for node in nodes:
                                level = int(node[2])
                                html.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                                value = node[0]
                                nodes = ebayDB.selectIdbyParent(self.tableName + str(6), value)
                                #print(nodes)

                            html.write("\t" * level + "<div>\n".format(node[2]))
                        html.write("\t" * level + "<div>\n".format(node[2]))
                    html.write("\t" * level + "<div>\n".format(node[2]))
                html.write("\t" * level + "<div>\n".format(node[2]))
            html.write("<\div>\n")

        else:
            print('CategoryID Not Found in CategoryLevel' + str(level))

        ebayDB.close()
        html.close()

        if found == False:
            print("*" * 15 + " CategoryID Not Found" + " " + "*" * 15)
            sys.exit("*" * 15 + " Terminate Script" + " " + "*" * 15)
