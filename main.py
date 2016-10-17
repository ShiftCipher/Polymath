#!/usr/bin/env python

__author__      = "Daniel Tarazona"
__copyright__   = "Copyright 2016, Codeapps"

import curl
import env
import db
import XML
import sys

def main():
    if sys.argv[0] == "generate":
        ebayDB = DB('ebay')
        ebayHeaders = {
            'X-EBAY-API-CALL-NAME' : 'GetCategories',
            'X-EBAY-API-APP-NAME' : env('APP_NAME'),
            'X-EBAY-API-CERT-NAME' : env('CERT_NAME'),
            'X-EBAY-API-DEV-NAME' : env('EBAY_API_DEV_NAME'),
            'X-EBAY-API-SITEID' : '0',
            'X-EBAY-API-COMPATIBILITY-LEVEL' : '861',
            'Content-Type' : 'text/xml'
        }
        ebayXML = XML('ebayGetCategories')
        ebayXML.setRequesterCredentials("EBAY_AUTH_TOKEN")
        ebayAPI = CURL(env('EBAY_API_ENDPOINT'))
        ebayCategoryArray = ebayAPI.requestXML(ebayHeaders, ebayXML)
        ebayDB.close()
    elif len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            ebayDB.drop()
            ebayDB.create()
        elif sys.argv[1] == "--render":
            categoryId = arg[2]
            render.tree(ebayDB.name, categoryId)

if __name__ == "__main__":
    main()
