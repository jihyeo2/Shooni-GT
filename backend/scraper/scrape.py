#!/usr/bin/env python3

# reference: https://www.geeksforgeeks.org/web-scraping-without-getting-blocked/

import requests

# use to parse html text
from lxml.html import fromstring
from itertools import cycle
import traceback

import random
import sys


def to_get_proxies():
    # website to get free proxies
    url = 'https://free-proxy-list.net/'

    response = requests.get(url)

    parser = fromstring(response.text)
    # using a set to avoid duplicate IP entries.
    proxies = set()

    count = 0
    print("proxy search begins")

    for i in parser.xpath('//tbody/tr')[:10]:

        print(count)
        count += 1

        # print(i.xpath('.//td[1]/text()')[0])
        # to check if the corresponding IP is of type HTTPS
        if i.xpath('.//td[7][contains(text(),"yes")]'):
        # if i.xpath('.//td[3][contains(text(),"HTTP")]'):

            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])

            print("found a proxy: ", proxy)

            proxies.add(proxy)
    return proxies

proxies = to_get_proxies()
while (len(proxies) < 6):
    proxies = to_get_proxies()
    print("Retrying proxy fetch")

print("Got enough proxy list")

# to rotate through the list of IPs
# proxyPool = cycle(proxies)

# print("len: ", len(proxies))
# for i in proxies:
#     print("proxy: ", i)
# insert the url of the website you want to scrape.
if (len(sys.argv) != 2):
    print("usage: ./scrape.py \{url\}")
    sys.exit()
else:
    url = sys.argv[1]

for i in range(1, 11):

    # Get a proxy from the pool
    proxy = random.choice(list(proxies)) # next(proxyPool)
    print("Request ", i , " with ", proxy)

    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(response.json())
        sys.exit()

    except:
	
        # One has to try the entire process as most
        # free proxies will get connection errors
        # We will just skip retries.
        print("Skipping. Connection error")
