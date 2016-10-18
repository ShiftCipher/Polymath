#!/usr/bin/env python

__author__     = "Daniel Tarazona"
__copyright__  = "Copyright 2016, Codeapps"

import db
import api
import request
import sys
from env import env

def main():



    '''
    header = request.Head()
    header.addHeader('X-EBAY-API-CALL-NAME', 'GetCategories')
    header.addHeader('X-EBAY-API-APP-NAME', env('APP_NAME'))
    header.addHeader('X-EBAY-API-CERT-NAME', env('CERT_NAME'))
    header.addHeader('X-EBAY-API-DEV-NAME', env('EBAY_API_DEV_NAME'))
    header.addHeader('X-EBAY-API-SITEID', '0')
    header.addHeader('X-EBAY-API-COMPATIBILITY-LEVEL', '989')
    header.addHeader('Content-Type', 'text/xml')
    ebayAPIGetCategoriesHeaders = header.getAll()
    ebayAPIGetCategoriesData = request.Body('ebayGetCategories', 'EBAY_AUTH_TOKEN').getXML()
    ebayAPICategories = ebayAPI.requestXML(ebayAPIGetCategoriesHeaders, ebayAPIGetCategoriesData)
    '''

    ebayDB = db.DB('ebay')
    ebayDB.connect()
    ebayDB.bulkCreate()
    ebayDB.bulkInsert('Category', 'xml/ebayCategories.xml')
    ebayDB.commit()
    print(ebayDB.getTableInfo('CategoryLevel3'))
    ebayDB.close()

if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            ebayDB.drop()
            ebayDB.create()
            main()
        elif sys.argv[1] == "--render":
            categoryId = str(sys.argv[2])
            print(categoryId)
