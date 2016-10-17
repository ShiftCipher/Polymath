#!/usr/bin/env python

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import os
import time
import parse

from env import env

class CURL(object):

    """docstring for CURL."""

    def __init__(self, url):
        self.root = "xml/"
        self.url = url
        self.request = None
        self.response = None

    def requestXML(self, headers, data):
        if isinstance(headers, dict) and isinstance(data, ascii):
            try:
                self.request = urllib.request.Request(self.url, headers=headers, data=data)
                self.response = urllib.request.urlopen(self.request)
                download = True
                time = 1
                while(download):
                    if isinstance(self.response, str):
                        download = False
                        print('Download Complete')
                        return self.response
                    else:
                        print("Downloading %s" % time)
                        time.sleep(1)
                        time =+ 1

            except urllib.error.URLError as e:
                print(e.reason)
        else:
            print("Headers needs be Type Dictionary and Data Type String")

    def exportXML(self, name, xml):
        if isinstance(name, str) and isinstance(xml, str):
            path = self.root + name + ".xml"
            if os.path.isfile(path):
                os.remove(path)
            try:
                print("Creating %s" % path)
                file = open(path, "w+")
                file.write(xml)
                file.close()
            except Exception as e:
                raise

    def parseXML(self, tag):
        context = ET.iterparse(self.response, events=('end',))
        for event, elem in context:
            if re.sub('{.*?}', '', elem.tag) == tag:
                for item in elem:
                    print(item.tag)
                    print(item.text)
                elem.clear()

headers = {
    'X-EBAY-API-CALL-NAME' : 'GetCategories',
    'X-EBAY-API-APP-NAME' : env('APP_NAME'),
    'X-EBAY-API-CERT-NAME' : env('CERT_NAME'),
    'X-EBAY-API-DEV-NAME' : env('EBAY_API_DEV_NAME'),
    'X-EBAY-API-SITEID' : '0',
    'X-EBAY-API-COMPATIBILITY-LEVEL' : '861',
    'Content-Type' : 'text/xml'
}

ebayXMLRequest = parse.Parse('ebayGetCategories', env('EBAY_AUTH_TOKEN'))
ebayXMLRequest = ebayXMLRequest.getXML()
print(ebayXMLRequest)
ebayAPI = CURL(env('EBAY_API_URL'))
ebayXMLCategories = ebayAPI.requestXML(headers, ebayXMLRequest)
ebayAPI.exportXML('Categories', ebayXMLCategories)
