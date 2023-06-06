# print("""Im Iron man.
# No I'm Niki.
# You are Jeni""")
# print("I'm Iron Man. \n" + "No Im Niki. \n" + "No Im Jeni. \n")
# print("Im Niki \n" * 5)
# from datetime import datetime
#
# now = datetime.now()
#
# current_year = now.year
# current_month = now.month
# current_day = now.day
# date = '%02d/%02d/%04d' % (now.month, now.day, now.year)
#
# print(f"Hello, welcome to Starbucks Coffee today the {date}!")
#
# name = input("What is your Name? \n")
# menu = "Black Coffee, Espresso, Latte, Cappuccino."
#
# if name == "Ben":
#     print(f"Fuck of {name}!")
#     exit("")
# else:
#     print('Hello, {}! What would it be?\nWe are serving {}'.format(name, menu))
# order = input()
# price = 8
# quantity = int(input("How many would you like ?\n"))
#
# total = price * int(quantity)
# print("Sounds good " + name + ", we'll have your " + str(quantity) + " " + order + " ready for you in a minute.")
# print(f"That would be ${total}.".lower())

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
