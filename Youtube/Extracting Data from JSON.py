# Read user input
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter : ")
print("Retrieving ", url)
data = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0
# Logic
for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1
# Output
print('Count:', total_number)
print('Sum:', sum)

