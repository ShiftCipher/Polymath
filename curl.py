#!/usr/bin/env python

import urlib2

class curl(object):
    """docstring for CURL."""

    def __init__(self, url):
        super(CURL, self).__init__()
        self.url = url
        self.request()

    def request(self):
        return urllib2.Request(self.url)

    def requestXML(self, headers, xml):
        if type(headers) is dict:
            for header in headers:
                req.add_header(header)
                req.add_xml(xml)
            res = urllib2.urlopen(req)
            return res.read()
