import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
xml = urllib.request.urlopen(url, context=ctx).read()

total = 0

data = ET.fromstring(xml)
tree_list = data.findall('comments/comment')
print('Number of commentators:', len(tree_list))


for node in tree_list:
        number = int(node.find('count').text)
        total = total + number
        print('Count is:', number, ', Total is: ', total)
