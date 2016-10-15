#!/usr/bin/env python

import urlib2

def getRequest(url, headers, xml):
    req = urllib2.Request(url)
    for header in headers:
        req.add_header(header)
        req.add_xml(xml)
        res = urllib2.urlopen(req)
    return res.read()
