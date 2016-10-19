#!/usr/bin/env python

__author__     = "Daniel Tarazona"
__copyright__  = "Copyright 2016, Codeapps"

import db
import api
import request
import sys

from env import env

def download():
    ebayAPI = api.API('EBAY_API')

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

    return ebayAPI.requestXML(headers, body)

def export():
    ebayAPI = download()
    ebayAPI.exportXML('GetCategories')

def rebuild():
    ebayDB = db.DB('ebay')
    ebayDB.drop()
    ebayDB.create()

def render(categoryId):
    import render
    ebayTree = render.Tree('CategoryLevel', categoryId)
    ebayTree.toHTML()

def populate():
    ebayDB = db.DB('ebay')
    ebayDB.connect()
    ebayDB.bulkCreate()
    ebayDB.bulkInsert('Category', 'xml/ebayCategories.xml')
    ebayDB.commit()
    ebayDB.close()

def main():
    populate()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        main()

    elif len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            download()
            export()
            rebuild()
            main()

        elif sys.argv[1] == "--export":
            export()

        elif sys.argv[1] == "--download":
            download()

        elif sys.argv[1] == "--render":
            categoryId = str(sys.argv[2])
            render(categoryId)

        ## 550 Root
        ## 13900 Level6 - 1 Root
        ## 13897 Level3
