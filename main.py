#!/usr/bin/env python

__author__      = "Daniel Tarazona"
__copyright__   = "Copyright 2016, Codeapps"

import curl
import env
import db
import render
import sys
import parse

fields = {
    'BestOfferEnabled' : 'INTEGER', # Store as 1 or 0
    'AutoPayEnable' : 'INTEGER', # Store as 1 or 0
    'CategoryID' : 'INTEGER',
    'CategoryName' : 'VARCHAR(255)',
    'CategoryParentID' : 'INTEGER'
}

url = "https://api.sandbox.ebay.com/ws/api.dll"

headers = {
    'X-EBAY-API-CALL-NAME' : 'GetCategories',
    'X-EBAY-API-APP-NAME' : env('APP_NAME'),
    'X-EBAY-API-CERT-NAME' : env('CERT_NAME'),
    'X-EBAY-API-DEV-NAME' : env('EBAY_API_DEV_NAME'),
    'X-EBAY-API-SITEID' : '0',
    'X-EBAY-API-COMPATIBILITY-LEVEL' : '861',
    'Content-Type' : 'text/xml'
}

xml = """<?xml version="1.0" encoding="utf-8"?>
<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
<RequesterCredentials>
<eBayAuthToken>""" + env('EBAY_AUTH_TOKEN') + """</eBayAuthToken>
</RequesterCredentials>
<CategorySiteID>0</CategorySiteID>
<DetailLevel>ReturnAll</DetailLevel>
</GetCategoriesRequest>"""

def main():
    if sys.argv[0] == "generate":
        ebayDB = DB('ebay')
        ebayAPI = CURL('https://api.sandbox.ebay.com/ws/api.dll')
        ebayCategoryArray = ebayAPI.requestXML(headers, xml)
        ebayDB.close()
    elif len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            ebay.drop()
            ebay.create()
        elif sys.argv[1] == "--render":
            categoryId = arg[2]
            render.tree(ebayDB.name, categoryId)




if __name__ == "__main__":
    main()
