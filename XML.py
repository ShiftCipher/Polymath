import os
import re
import xml.etree.ElementTree as ET
from env import env

class XML(object):

    """docstring for XML."""

    def __init__(self, path):
        self.path = None
        self.tree = None
        self.root = None
        self.name = None
        self.namespace = None

        if isinstance(path, str):
            path = 'xml/' + path + ".xml"
            try:
                if os.path.isfile(path):
                    self.path = path
                    self.tree = ET.parse(self.path)
                    self.root = self.tree.getroot()
                    self.name = self.getRequestName()
                    self.namespace = self.getNamespace()
                else:
                    print("File name not Found")
            except Exception as e:
                raise
        else:
            print("File name must be a String")

    def getRequestName(self):
        return re.sub('{.*?}', '', self.root.tag)

    def getNamespace(self):
        return self.root.tag.split('}')[0].strip('{')

    def setRequesterCredentials(self, token):
        if isinstance(token, str) and self.root != None:
            try:
                self.root[0][0].text = env(token)
                self.tree.write(self.path)
            except Exception as e:
                raise
