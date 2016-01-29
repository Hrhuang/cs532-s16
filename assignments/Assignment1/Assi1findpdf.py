#!/usr/bin/env python
import urllib2
import sys
import requests
from bs4 import BeautifulSoup
#http://www.cs.odu.edu/~mln/teaching/cs532-s16/test/pdfs.html
#http://docs.python-requests.org/en/latest/api/#requests.Response

weburl = sys.argv[1]

gett = requests.get(weburl)
html = gett.text

soup = BeautifulSoup(html)
links = soup.find_all('a')

def getHeaders(link):

    try:
        response = requests.get(link)
        if response.headers['content-type'] == 'application/pdf':
            print "The URL is: ", response.url
            print "The final response code is: ", response.status_code
            print "The content type is: ", response.headers['content-type']
            print "The file size is: ", response.headers['content-length']
            print "The redirection code is: ", response.history
    except Exception:
        return
    #print "Response:", response
    #print "The Headers are: ", response.headers
    #print "The Date is: ", response.headers['date']
    #print "The Server is: ", response.headers['server']
    #html = response.read()

for tag in links:
    link = tag.get('href',None)
    getHeaders(link);

#by Huan Huang