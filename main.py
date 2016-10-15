#!/usr/bin/env python

__author__      = "Daniel Tarazona"
__copyright__   = "Copyright 2016, Codeapps"

import curl
import env
import db
import render
import sys

url = "https://api.sandbox.ebay.com/ws/api.dll"

headers = {
    'X-EBAY-API-CALL-NAME:' : 'GeteBayOfficialTime',
    'X-EBAY-API-APP-NAME:' : env('APP_NAME'),
    'X-EBAY-API-CERT-NAME:' : env('CERT_NAME'),
    'X-EBAY-API-DEV-NAME:' : env('DEV_NAME'),
    'X-EBAY-API-SITEID:' : '0',
    'X-EBAY-API-COMPATIBILITY-LEVEL:' : '861'
}

xml = """
<?xml version="1.0" encoding="utf-8"?>
<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
  <eBayAuthToken>""" + env('AUTH_TOKEN') + """</eBayAuthToken>
  </RequesterCredentials>
  <CategorySiteID>0</CategorySiteID>
  <DetailLevel>ReturnAll</DetailLevel>
</GetCategoriesRequest>
xmllint --format -
"""

def get_ebay_category_array(url, headers, xml):
    return curl(url, headers, xml)

def bulk(LevelArray, CategoryArray):
    for Level in LevelArray:
        for Category in ebayCategoryArray:
        ebay.query('Level', 'create')
            ebay.query('Level', 'insert', 'Category')
                # BestOfferEnabled bool
                # AutoPayEnable bool
                # CategoryID integer
                # CategoryName string
                # CategoryParentID integer

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            ebay.drop()
            ebay.create()
        elif sys.argv[1] == "--render":
            categoryId = arg[2]
            render.tree(ebay.name, categoryId)
    else:
        ebay = DB('ebay')
        CategoryArray = get_ebay_category_array()
        ebay.query()
        ebay.close()


if __name__ == "__main__":
    main()
