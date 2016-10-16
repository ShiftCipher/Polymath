#!/usr/bin/env python

import urllib.request
import urllib.parse
import urllib.error
import json
from env import env

class CURL(object):

    """docstring for CURL."""

    def __init__(self, url):
        self.url = url
        self.request = None
        self.response = None

    def requestXML(self, headers, data):
        if isinstance(headers, dict) and isinstance(data, str):
            data = data.replace("\n", "")
            data = data.encode('ascii')
            try:
                print("Fetching...")
                self.request = urllib.request.Request(self.url, headers=headers, data=data)
                self.response = urllib.request.urlopen(self.request).read()
                return self.response
            except urllib.error.URLError as e:
                print(e.reason)
        else:
            print("Headers needs be Type Dictionary and Data Type String")
