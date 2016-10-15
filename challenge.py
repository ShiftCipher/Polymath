#!/usr/bin/env python

import curl
import env
import db

if os.path.isfile("ebay.bd"):

url = "https://api.sandbox.ebay.com/ws/api.dll"

headers = [
    'X-EBAY-API-CALL-NAME: GeteBayOfficialTime',
    'X-EBAY-API-APP-NAME: ' + env('APP_NAME'),
    'X-EBAY-API-CERT-NAME: ' + env('CERT_NAME'),
    'X-EBAY-API-DEV-NAME: ' + env('DEV_NAME'),
    'X-EBAY-API-SITEID: 0',
    'X-EBAY-API-COMPATIBILITY-LEVEL: 861'
]

xml = """
<?xml version="1.0" encoding="utf-8"?>
<GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
  <eBayAuthToken>env('APP_KEY')</eBayAuthToken>
  </RequesterCredentials>
  <CategorySiteID>0</CategorySiteID>
  <DetailLevel>ReturnAll</DetailLevel>
</GetCategoriesRequest>
xmllint --format -
"""

# CLI arg[0] --rebuild
    # IF 'ebay' EXISTS IN DIR
        # DELETE



try:
    ebay = DB('ebay')
except Exception as e:
    raise
else:
    DB('ebay').drop()

ebay.connect()
ebayCategoryArray = curl.request(url, headers, xml)


ebay.commit()
ebay.close()

for CategoryLevel in ebayCategoryArray:
    ebay.query('Level', 'create')
        ebay.query('Level', 'insert', 'Category')
            # BestOfferEnabled bool
            # AutoPayEnable bool
            # CategoryID integer
            # CategoryName string
            # CategoryParentID integer
        # conn.commit()
# CLOSE DATABASE

# CLI arg[1] --render <category_id>
    # $categoryId = <category_id>
    # def searchCategoryId(id)
        # L1 = 35
        # if (id > AggregateNode)

        # SEARCH <category_id> IN CategoryLevel
        # GENERATE <category_id>.html
        # CATEGORY TREE ROOTED



try:
    conn = sqlite3.connect('challenge.db')
except IOError:
    print('cannot connect')
else:
    print a
    f.close()


conn.execute('''CREATE TABLE categories
             (date text, trans text, symbol text, qty real, price real)''')




$CategoryArray = exec(open("get_ebay_official_time").read())

os.

file = open(category + ".html", "w+")
    file.write(name);
file.close()
