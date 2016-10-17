#!/usr/bin/env python

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import os
import re
import time
import request
from env import env

class API(object):

    """docstring for API."""

    def __init__(self, url):
        self.root = "xml/"
        self.url = env(url)
        self.request = None
        self.response = None
        self.export = None

    def requestXML(self, headers, data):
        if isinstance(data, str) and isinstance(headers, dict):
            data = data.encode('ascii')
            try:
                self.request = urllib.request.Request(self.url, headers=headers, data=data)
                self.response = urllib.request.urlopen(self.request).read()
                download = True
                clock = 1
                while(download):
                    if isinstance(self.response, bytes):
                        download = False
                        print('Download Complete Total Time %s' % clock)
                        return self.response
                    else:
                        print("Downloading %s" % clock)
                        time.sleep(1)
                        clock += 1
            except urllib.error.URLError as e:
                print(e.reason)

    def parseXMLColumns(self, tag, path):
        tree = ET.parse(path).getroot()
        columns = {}
        for elem in tree[4][0]:
            tag = re.sub('{.*?}', '', elem.tag)
            text = re.sub('{.*?}', '', elem.text)
            print(tag, text)
            try:
                if (isinstance(text, float)):
                    columns[tag] = 'NUMERIC'
                elif (text == "true" or text == "false"):
                    columns[tag] = 'NUMERIC'
                elif (isinstance(text, str)):
                    columns[tag] = 'TEXT'
                elif (isinstance(text, int)):
                    columns[tag] = 'INTEGER'
            except Exception as e:
                raise
        return columns

    def exportXML(self, name):
        if isinstance(name, str):
            try:
                self.export = path
                path = "xml/" + name + ".xml"
                print("Creating %s" % path)
                file = open(path, "w+")
                file.write(self.response.decode('utf-8'))
                file.close()
            except Exception as e:
                raise
