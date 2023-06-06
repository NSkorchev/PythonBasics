# Read user input
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# Logic
url = input('Enter : ')
print ("Retrieving", url)
html = urllib.request.urlopen(url, context=ctx)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
comment_count=len(results)
sum_numbers=0

for result in results:
    sum_numbers += float(result.find('count').text)
# Output
print(comment_count)
print(sum_numbers)



