13900#!/usr/bin/env python

__author__     = "Daniel Tarazona"
__copyright__  = "Copyright 2016, Codeapps"

import db
import api
import request
import sys

from env import env

def download():
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
    ebayAPI = api.API('EBAY_API_URL')
    ebayAPI.requestXML(headers, body)
    return ebayAPI

def export():
    ebayAPI.exportXML('GetCategories')

def rebuild():
    ebayDB = db.DB('ebay')
    ebayDB.drop()
    ebayDB.create()
    ebayDB.connect()
    return ebayDB

def render(categoryId):
    import render
    ebayTree = render.Tree('CategoryLevel', categoryId)
    ebayTree.toHTML()

def populate():
    ebayDB = rebuild()
    ebayDB.bulkCreate()
    ebayDB.bulkInsert('Category', 'xml/GetCategories.xml')
    ebayDB.commit()
    ebayDB.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            rebuild()
            download()
            populate()

        elif sys.argv[1] == "--download":
            download()
            export()

        elif sys.argv[1] == "--render":
            categoryId = str(sys.argv[2])
            render(categoryId)
    else:
        sys.exit("ERROR No Arguments Passed")

        ## 550 Root
        ## 13900 Level6 - 1 Root
        ## 13897 Level3
