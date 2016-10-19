#!/usr/bin/env python

import db
import sys

def getTreeRoot(categoryId):
    ebayDB = db.DB('ebay')
    ebayDB.connect()

    #print(ebayDB.getTableInfo('CategoryLevel6'))

    found = False

    for level in range(1, 7):
        table = 'CategoryLevel'
        node = ebayDB.selectOneId(table + str(level), categoryId)
        if node != None:
            print("*" * 10 + " Found in CategoryLevel" + str(level) + " " + "*" * 10)
            print("ROOT")
            found = True
            steps = abs(1 - int(node[2])) + 1
            print(node)
            for value in range(1, steps):
                node = ebayDB.selectOneId(table + str(int(node[2]) - 1), node[1])
                print(node)
            print("TREE")
        else:
            print('CategoryID Not Found in CategoryLevel' + str(level))
    ebayDB.close()

    if found == False:
        print("*" * 15 + " CategoryID Not Found" + " " + "*" * 15)
        sys.exit("*" * 15 + " Terminate Script" + " " + "*" * 15)

def getTreeLeaf(categoryId, path):
    ebayDB = db.DB('ebay')
    ebayDB.connect()

    found = False
    table = 'CategoryLevel'
    file = open("html/" + path + ".html" , "w+")

    def getLeafNodes(nodes, level):
        while(level < 7):
            leafs = []
            level += 1
            for node in nodes:
                file.write("\t" * level + "<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                value = node[0]
                if level < 7:
                    leafs = ebayDB.selectIdbyParent(table + str(level), value)
                    getLeafNodes(leafs, level)
            file.write("\t" * level + "</div>\n")

    def getRootNode(categoryId):
        node = []
        for level in range(1, 7):
            node = ebayDB.selectOneId(table + str(level), categoryId)
            if node != None:
                found = True
                print("*" * 15 + " CategoryID Found %s" % str(level) + " " + "*" * 15)
                file.write("<div class=L{0}>{1} {2} {3} {4}\n".format(node[2], node[0], node[3], node[2], node[4]))
                return [node]
                file.write("</div>\n")

    rootNode = getRootNode(categoryId)
    print(rootNode)
    getLeafNodes(rootNode, int(rootNode[0][2]))

    file.close()
    ebayDB.close()

    if found == False:
        print("*" * 15 + " CategoryID Not Found" + " " + "*" * 15)
        sys.exit("*" * 15 + " Terminate Script" + " " + "*" * 15)
