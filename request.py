#!/usr/bin/env python

import os
import re
import xml.etree.ElementTree as ET
from env import env

class Body(object):

    """docstring for Request."""

    def __init__(self, path, token):
        self.path = ""
        self.name = ""
        self.tree = None
        self.root = None
        self.namespace = ""

        if isinstance(path, str) and isinstance(token, str):
            try:
                self.path = 'xml/' + path + '.xml'
                if os.path.isfile(self.path):
                    self.tree = ET.parse(self.path)
                    self.root = self.tree.getroot()
                    self.name = self.getRequestName()
                    self.namespace = self.getNamespace()
                    self.setNamespace()
                    self.setCategorySiteID(0)
                    self.setRequesterCredentials(token)
                else:
                    print("Filename and Token must be Strings")
            except Exception as e:
                raise
        else:
            print('Args must be Strings')

    def getRequestName(self):
        return re.sub('{.*?}', '', self.root.tag)

    def getNamespace(self):
        return self.root.tag.split('}')[0].strip('{')

    def setNamespace(self):
        return ET.register_namespace("", self.namespace)

    def setCategorySiteID(self, siteId):
        try:
            if isinstance(siteId, int):
                for elem in self.root.iter():
                    if re.sub('{.*?}', '', elem.tag) == 'CategorySiteID':
                        elem.text = str(siteId)
                self.tree.write(self.path, encoding="utf-8", method="xml")
                #print('Set CategorySiteID to %s' % str(siteId))
        except Exception as e:
            raise

    def setRequesterCredentials(self, token):
        try:
            if isinstance(token, str) and self.root != None:
                for elem in self.root.iter():
                    if re.sub('{.*?}', '', elem.tag) == 'eBayAuthToken':
                        elem.text = env(token)
                self.tree.write(self.path, encoding="utf-8", method="xml")
                #print('Set Requester Credentials')
        except Exception as e:
            raise

    def getXML(self):
        try:
            if self.root != None:
                xml = ET.tostring(self.root, encoding='utf-8', method="xml")
                xml = xml.decode('utf-8')
                xml = '<?xml version=\'1.0\' encoding=\'utf-8\'?>' + xml[0:]
                xml = xml.replace("\n", "")
                return str(xml)
        except Exception as e:
            raise

class Head(object):

    """docstring for HEAD"""

    def __init__(self):
        self.all = {}

    def addHeader(self, name, value):
        if isinstance(name, str) and isinstance(value, str):
            self.all[name] = value

    def getHeader(self, name):
        return self.all[name]

    def getAll(self):
        return self.all
