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
        self.url = None
        self.request = None
        self.response = bytes()
        self.export = None
        self.download = False
        self.getURL(url)

    def getURL(self, url):
        if isinstance(url, str):
            self.url = env(url)
            return self.url

    def requestXML(self, headers, data):
        if isinstance(data, str) and isinstance(headers, dict):
            data = data.encode('ascii')
            try:
                self.request = urllib.request.Request(self.url, headers=headers, data=data)
                self.response = urllib.request.urlopen(self.request).read()
                self.download = True
                clock = 1
                while(self.download):
                    time.sleep(1)
                    clock += 1
                    if isinstance(self.response, bytes):
                        self.download = False
                        print('Download Complete Total Time %ss' % clock)
                        return self.response
            except urllib.error.URLError as e:
                print(e.reason)

    def exportXML(self, name):
        if isinstance(name, str):
            try:
                path = "xml/" + name + ".xml"
                self.export = path
                print("Creating %s.xml" % name )
                file = open(path, "w+")
                file.write(self.response.decode('utf-8'))
                file.close()
            except Exception as e:
                raise

    def requestXMLColumnsName(self, tag, path):
        if isinstance(tag, str):
            tree = ET.iterparse(path, events=('end',))
            for event, elem in tree:
                if re.sub('{.*?}', '', elem.tag) == tag:
                    names = {}
                    for item in elem:
                        tag = re.sub('{.*?}', '', item.tag)
                        names[tag] = tag
                    names = ", ".join(names)
                    elem.clear()
                    return names
