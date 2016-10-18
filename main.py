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

    #print(ebayDB.getTableInfo('CategoryLevel3'))

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

    for level in range(1, 7):
        table = 'CategoryLevel'
        node = ebayDB.selectOneId(table + str(level), categoryId)
        if node != None:
            position = abs(7 - int(node[2]))
            print("POSITION %s" % position)
            print(node[0], node[1])
            for value in range(1, position):
                node = ebayDB.selectIdbyParent(table + str(position), node[0])
                print(node)

        else:
            print('CategoryID Not Found in CategoryLevel' + str(level))
    ebayDB.close()

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

        elif sys.argv[1] == "--export":
            print(True)
