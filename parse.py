#!/usr/bin/env python

import os
import re
import xml.etree.ElementTree as ET
from env import env

class Parse(object):

    """docstring for XML."""

    def __init__(self, path, token):
        self.path = None
        self.name = None
        self.tree = None
        self.root = None
        self.namespace = None

        if isinstance(path, str) and isinstance(token, str):
            self.path = 'xml/' + path + ".xml"
            try:
                if os.path.isfile(self.path):
                    self.tree = ET.parse(self.path)
                    self.root = self.tree.getroot()
                    self.name = self.getRequestName()
                    self.namespace = self.getNamespace()
                    self.setNamespace()
                    self.setRequesterCredentials(token)
                else:
                    print("File name not Found")
            except Exception as e:
                raise
        else:
            print("File name must be a String")

    def getXML(self):
        return ET.tostring(self.root, 'utf-8', method="xml")

    def getRequestName(self):
        return re.sub('{.*?}', '', self.root.tag)

    def getNamespace(self):
        return self.root.tag.split('}')[0].strip('{')

    def setNamespace(self):
        return ET.register_namespace("", self.namespace)

    def setRequesterCredentials(self, token):
        try:
            if isinstance(token, str) and self.root != None:
                self.root[0][0].text = env(token)
                self.tree.write(self.path)
        except Exception as e:
            raise
