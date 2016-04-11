from os.path import basename
#from urllib.parse import urljoin
from lxml import html
import requests

base_url = 'http://www.astridlindgrensallskapet.se/boka-visning/'

# v2
page = requests.get(base_url)
tree = html.fromstring(page.content)
test = tree.xpath('//script[@type="text/javascript"]/text()')

# == STEP 1 ==
# look for everything
#for i in test:
#    print(i.encode('utf-8'))


# == STEP 2 ===
# Look a
#raw = test[4]
#print(raw.encode('utf-8'))

# == STEP 3 ==
# get date

out = []

raw = test[4]
for t in raw.split(',,'):
     if 'SteelBlue' in t:
        #print(t.encode('utf-8'))
        tmp = t.split(',')
        dato = '-'.join(tmp[3:6])
        #print(dato[1:-1])
        out.append(dato[1:-1])


# Get exceptions from manual file
with open('./fully_booked.txt') as f:
    fully_booked = f.read().splitlines()
#print(fully_booked)
#fully_booked = ['2016-4-23']

new_dates = set(out) - set(fully_booked)

new_dates_string = [i.encode('utf-8') for i in list(new_dates)]
if new_dates_string:
    print('email_me')
    print(new_dates_string)




