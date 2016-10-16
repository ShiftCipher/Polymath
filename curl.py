#!/usr/bin/env python

import urllib.request
import urllib.parse
import json
from env import env

class curl(object):

    """docstring for CURL."""

    def __init__(self, url):
        self.url = url
        self.request = None
        self.response = None

    def requestXML(self, headers, data):
        try:
            if isinstance(headers, dict) and isinstance(data, dict):
                data = urllib.parse.urlencode(data).encode("utf-8")
                data = data.encode('ascii')
                self.request = urllib.request.Request(self.url, headers=headers, data=data)
                self.response = urllib.request.urlopen(self.request)
                return self.request
            else:
                print("XML has been String Type and Headers a Dictionary")
        except Exception as e:
            raise

headers = {
    'X-EBAY-API-CALL-NAME' : 'GetCategories',
    'X-EBAY-API-APP-NAME' : env('APP_NAME'),
    'X-EBAY-API-CERT-NAME' : env('CERT_NAME'),
    'X-EBAY-API-DEV-NAME' : env('EBAY_API_DEV_NAME'),
    'X-EBAY-API-SITEID' : '0',
    'X-EBAY-API-COMPATIBILITY-LEVEL' : '861',
    'Content-Type' : 'text/xml'
}

data = {
   "GetCategoriesRequest": {
      "RequesterCredentials": {
         "eBayAuthToken": env('EBAY_AUTH_TOKEN')
      },
      "CategorySiteID": "0",
      "DetailLevel": "ReturnAll",
      "_xmlns": "urn:ebay:apis:eBLBaseComponents"
   }
}

ebayAPI = curl('https://api.sandbox.ebay.com/ws/api.dll')
ebayAPI.requestXML(headers, data)
print(ebayAPI.request)
