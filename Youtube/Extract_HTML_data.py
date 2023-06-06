# Read user input
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count -'))
pos = int(input('Enter position -')) - 1
urllist = list()
taglist = list()
# Logick
for i in range(count):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieveing:', url)
    taglist = list()
    for tag in tags:
        y = tag.get('href', None)
        taglist.append(y)

    url = taglist[pos]

    urllist.append(url)
# Output
print("Last Url:", urllist[-1])
