#!/usr/bin/env python

import urlib2

class curl(object):

    """docstring for CURL."""

    def __init__(self, url):
        super(CURL, self).__init__()
        self.url = url
        self.req = None
        self.cur = None
        self.request()

    def request(self):
        try:
            self.req = urllib2.Request(self.url)
            self.cur = self.req.cursor()
            return self.cur
        except Exception as e:
            raise

    def requestXML(self, headers, xml):
        try:
            if isinstance(xml, str) and isinstance(headers, dict):
                for header, value in headres.items():
                    self.cur.add_header(header[value])
                    form = {'XML': xml}
                    data = urllib.urlencode(form)
                    self.cur.add_data(xml)
                res = urllib2.urlopen(req)
                return res.read()
            else:
                print("XML has been String Type and Headers a Dictionary")
        except Exception as e:
            raise

headers = {
    'X-EBAY-API-CALL-NAME:' : 'GeteBayOfficialTime',
    'X-EBAY-API-APP-NAME:' : env('APP_NAME'),
    'X-EBAY-API-CERT-NAME:' : env('CERT_NAME'),
    'X-EBAY-API-DEV-NAME:' : env('EBAY_API_DEV_NAME'),
    'X-EBAY-API-SITEID:' : '0',
    'X-EBAY-API-COMPATIBILITY-LEVEL:' : '861'
}

xml = """
<?xml version="1.0" encoding="utf-8"?>
<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
  <eBayAuthToken>""" + env('EBAY_AUTH_TOKEN') + """</eBayAuthToken>
  </RequesterCredentials>
  <CategorySiteID>0</CategorySiteID>
  <DetailLevel>ReturnAll</DetailLevel>
</GetCategoriesRequest>
"""

ebayAPI = curl('https://api.sandbox.ebay.com/ws/api.dll')
ebayAPI.requestXML(headers, xml)
