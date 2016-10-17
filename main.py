#!/usr/bin/env python

__author__     = "Daniel Tarazona"
__copyright__  = "Copyright 2016, Codeapps"

import curl
import db
import curl
import request
import sys
from env import env

def main():
    ebayAPI = curl.API('EBAY_API_URL')
    #header = request.Head()
    #header.addHeader('X-EBAY-API-CALL-NAME', 'GetCategories')
    #header.addHeader('X-EBAY-API-APP-NAME', env('APP_NAME'))
    #header.addHeader('X-EBAY-API-CERT-NAME', env('CERT_NAME'))
    #header.addHeader('X-EBAY-API-DEV-NAME', env('EBAY_API_DEV_NAME'))
    #header.addHeader('X-EBAY-API-SITEID', '0')
    #header.addHeader('X-EBAY-API-COMPATIBILITY-LEVEL', '989')
    #header.addHeader('Content-Type', 'text/xml')
    #ebayAPIGetCategoriesHeaders = header.getAll()
    #ebayAPIGetCategoriesData = request.Body('ebayGetCategories', 'EBAY_AUTH_TOKEN').getXML()
    #ebayAPICategories = ebayAPI.requestXML(ebayAPIGetCategoriesHeaders, ebayAPIGetCategoriesData)
    ebayDB = db.DB('ebay')
    ebayDB.connect()

    columns = ebayAPI.parseXMLColumns('Category', 'xml/ebayCategories.xml')
    ebayDB.createTablesByColumn('CategoryLevel', columns, 6)
    columnsName = " ".join(columns.keys())
    ebayDB.parseXML('Category', columnsName, 'xml/ebayCategories.xml')

    ebayDB.commit()

    # ebayAPI.exportXML('ebayCategories')
    ebayDB.close()
    if len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            ebayDB.drop()
            ebayDB.create()
        elif sys.argv[1] == "--render":
            categoryId = arg[2]
            render.tree(ebayDB.name, categoryId)

if __name__ == "__main__":
    main()
