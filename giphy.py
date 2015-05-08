#!/usr/bin/python

# -*- coding: utf8 -*-

import urllib2
import argparse
import json
import subprocess


giphy_key = 'dc6zaTOxFJmzC'


def parseArgs():
    parser = argparse.ArgumentParser(
        description="Randomly find a gif that match the given keywords. See: \
https://github.com/Giphy/GiphyAPI#translate-endpoint",
        prog="giphy.py")
    parser.add_argument('keywords', action='store', nargs='+',
                        help="The keyword(s) to translate into a gif.")
    parser.add_argument('-r', '--rating', action='store', default=None,
                        choices='y,g,pg,pg-13,r'.split(','),
                        help="Restrict the results to the given rating.")
    return parser.parse_args()


def request(url):
    req = urllib2.Request(url)

    handler = urllib2.urlopen(req)

    return handler.read()


def getGIF(keywords, rating=None):
    url = 'http://api.giphy.com/v1/gifs/translate?s=%s&api_key=%s'
    url = url % (keywords.replace(' ', '+'), giphy_key)
    if rating:
        url += '&rating=%s' % rating
    text = request(url)
    res = json.loads(text)
    if 'data' in res and len(res['data']) > 0:
        return res['data']['images']['downsized']['url']
    print "ERROR: Unable to find any gif matching the keywords: %s" \
        % (' '.join(keywords.split('+')))
    return ''


def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

ns = parseArgs()
url = getGIF('+'.join(ns.keywords), ns.rating)
setClipboardData(url)
if url:
    print "URL: %s saved to clipboard!" % url
