import urllib2
import errno
import socket 
import httplib
import ssl
import sys
import requests
from requests.exceptions import HTTPError

gett = open('initialurls.txt', 'r')
savefile = open('urlsRound2.txt', 'a')

s = socket.socket()
s.settimeout(5)

def getHeaders(urls):
	try: 
	    #conn = urllib2.urlopen(urls)
	    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
	    request = opener.open(urls)

	    print request.url
	    savefile.write(request.url)
	    savefile.write('\n')
	    #print request.code
	    
	except urllib2.HTTPError, x:
		print 'Ignoring', x.code
	except urllib2.URLError, e:
		print 'Ignoring', e.args
	except ssl.CertificateError, s:
		print 'Ignoring', s
	except socket.error, s:
		print 'Ignoring %s' % s
	except httplib.BadStatusLine, b:
		pass

for links in gett:
    urls = links
    getHeaders(urls);