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
        self.depth = 7

    def getRootLevel(self, DB):
        if DB != None:
            try:
                for level in range(1, self.depth):
                    node = DB.selectOneId(self.tableName + str(level), self.categoryId)
                    if node != None:
                        self.node = [node]
                        self.lvl = int(node[2])
                        self.found = True
                        return self.lvl
            except Exception as e:
                raise

    def getRootNodes(self, DB, html):
        if DB != None and isinstance(html, file)
            try:
                node = self.node[0]
                level = self.lvl
                nodes = []
                html.write("<html>\n\t<head>\n")
                html.write("\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n")
                html.write("\t\t<script type=\"text/javascript\" src=\"http://code.jquery.com/jquery.min.js\"></script>\n")
                html.write("\t\t<script src=\"http://code.jquery.com/ui/1.9.2/jquery-ui.min.js\"></script>\n")
                html.write("\t\t<script src=\"app.js\"></script>\n")
                html.write("\t</head>\n")
                html.write("\t<body>\n")
                html.write("\t\t<canvas id=\"canvas\"></canvas>\n")

                for level in range(1, self.depth):
                    node = DB.selectOneId(self.tableName + str(level), self.categoryId)
                    if node != None:
                        self.found = True
                        steps = abs(1 - int(node[2])) + 1
                        for value in range(1, steps):
                            node = DB.selectOneId(self.tableName + str(int(node[2]) - 1), node[1])
                            nodes.append(node)

                for node in reversed(nodes):
                    space = int(node[2]) + 2
                    html.write("\t" * space + "<div class=\"L{0}\">{1} {2} {3} {4}</div>\n".format(node[2], node[0], node[3], node[2], node[4]))
            except Exception as e:
                raise


    def getLeafNodes(self, nodes, DB, html):
        if DB != None and isinstance(html, file) and isinstance(nodes, tuple)
            try:
                level = self.lvl
                while(level < self.depth):
                    leafs = []
                    level += 1
                    for node in nodes:
                        space = int(node[2]) + 2
                        html.write("\t" * space + "<div class=\"L{0}\">\n".format(node[2]))
                        html.write("\t" * (space + 1) + "<p>{1} {2} {3} {4}</p>\n".format(node[2], node[0], node[3], node[2], node[4]))
                        value = node[0]
                        if level < self.depth:
                            leafs = DB.selectIdbyParent(self.tableName + str(level), value)
                            self.getLeafNodes(leafs, DB, html)
                        html.write("\t" * space + "</div>\n")
            except Exception as e:
                raise

    def closeHTML(self, html):
        if isinstance(html, file):
            try:
                for step in range(self.steps + 2, 0, -1):
                    html.write("\t" * step + "</div>\n")
                html.write("\t</body>\n")
                html.write("</html>")
                html.close()
            except Exception as e:
                raise

    def toHTML(self):
        try:
            ebayDB = db.DB('ebay')
            ebayDB.connect()

            self.getRootLevel(ebayDB)

            if self.found == True:
                html = open("html/" + self.categoryId + ".html" , "w+")
                self.getRootNodes(ebayDB, html)
                self.getLeafNodes(self.node, ebayDB, html)
                self.closeHTML(html)
            else:
                sys.exit("ERROR CategoryID NOT Found")
        except Exception as e:
            raise
