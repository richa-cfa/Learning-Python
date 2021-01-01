# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter webpage URL - ')
start_pos=int(input('Enter start position - '))
repeat_count = int(input('Enter repeat count - '))

counter = 1
parsed = re.findall('_by_(.*).html', url)
print('Start = ',counter, ", parsed name : ", parsed[0])


while counter < repeat_count+1 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    line = (tags[start_pos-1].decode())
    url = re.findall('href="(.*.html)">', line)[0]
    parsed = re.findall('_by_(.*).html', line)
    counter = counter +1
    print("Repeat = ", counter-1, ", parsed name : ", parsed[0], url)
