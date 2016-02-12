#!/usr/bin/env python2
import urllib2
import requests
from requests.exceptions import HTTPError


'''
weburl = sys.argv[1]

gett = requests.get(weburl)
html = gett.text
'''
gett = open('initialurls.txt', 'r')
savefile = open('urlsRoundV2.txt', 'a')

def getHeaders(urls):
   
    try:
        response = requests.get(urls, timeout=10)
       
        if response.status_code == 200:
	        print (response.url)
	        print ("The response code: ", response.status_code)
	        savefile.write(response.url)
	        savefile.write('\n')

            #print ("The content type is: ", response.headers['content-type'])  
            #print ("The file size is: ", response.headers['content-length'])
            #print ("The redirection code is: ", response.history])

    except Exception as e:
        print 'Ingoring :', e

    #print "Response:", response
    #print "The Headers are: ", response.headers
    #print "The Date is: ", response.headers['date']
    #print "The Server is: ", response.headers['server']
    #html = response.read()

for links in gett:
    urls = links
    getHeaders(urls);
