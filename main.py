#!/usr/bin/env python

__author__     = "Daniel Tarazona"
__copyright__  = "Copyright 2016, Codeapps"

import db
import api
import request
import sys
from env import env

def getCategoriesXML():
    header = request.Head()
    header.addHeader('X-EBAY-API-CALL-NAME', 'GetCategories')
    header.addHeader('X-EBAY-API-APP-NAME', env('APP_NAME'))
    header.addHeader('X-EBAY-API-CERT-NAME', env('CERT_NAME'))
    header.addHeader('X-EBAY-API-DEV-NAME', env('EBAY_API_DEV_NAME'))
    header.addHeader('X-EBAY-API-SITEID', '0')
    header.addHeader('X-EBAY-API-COMPATIBILITY-LEVEL', '989')
    header.addHeader('Content-Type', 'text/xml')
    body = request.Body('ebayGetCategories', 'EBAY_AUTH_TOKEN').getXML()
    headers = header.getAll()
    return (headers, body)

def getResponseXML():
    ebayAPI = api.API('EBAY_API')
    ebayAPI.requestXML(getCategoriesXML())
    return ebayAPI

def export():
    getResponseXML().exportXML('GetCategories')

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

def getTreeLeaf(categoryId):
    ebayDB = db.DB('ebay')
    ebayDB.connect()

    #print(ebayDB.getTableInfo('CategoryLevel2'))

    found = False
    start = int()
    table = 'CategoryLevel'

    for level in range(1, 7):
        node = ebayDB.selectOneId(table + str(level), categoryId)
        if node != None:
            start = int(node[2])

    render = {}

    for level in range(start, 7):
        node = ebayDB.selectOneId(table + str(level), categoryId)
        render[level] = node
        if node != None:
            node = node[0]
            nodes = ebayDB.selectIdbyParent(table + str(level + 1), node)
            render[level + 1] = nodes
            for value in nodes:
                value = value[0]
                nodes = ebayDB.selectIdbyParent(table + str(level + 2), value)
                render[level + 2] = nodes
                for value in nodes:
                    value = value[0]
                    nodes = ebayDB.selectIdbyParent(table + str(level + 3), value)
                    render[level + 3] = nodes
                    for value in nodes:
                        value = value[0]
                        nodes = ebayDB.selectIdbyParent(table + str(level + 4), value)
                        render[level + 4] = nodes
                        for value in nodes:
                            value = value[0]
                            nodes = ebayDB.selectIdbyParent(table + str(level + 5), value)
                            render[level + 5] = nodes

        else:
            print('CategoryID Not Found in CategoryLevel' + str(level))
    ebayDB.close()

    print(render)

    if found == False:
        print("*" * 15 + " CategoryID Not Found" + " " + "*" * 15)
        sys.exit("*" * 15 + " Terminate Script" + " " + "*" * 15)

def main():
    ebayDB = db.DB('ebay')
    ebayDB.connect()
    ebayDB.bulkCreate()
    ebayDB.bulkInsert('Category', 'xml/ebayCategories.xml')
    ebayDB.commit()
    ebayDB.close()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            ebayDB = db.DB('ebay')
            ebayDB.drop()
            ebayDB.create()
            main()
        elif sys.argv[1] == "--render":
            categoryId = str(sys.argv[2])
            getTreeRoot(categoryId)
            getTreeLeaf(categoryId)
            ## 550 Root
            ## 13900 Level6 - 1 Root
            ## 13897 Level3

        elif sys.argv[1] == "--export":
            print(True)
