import commands
import os, sys
import re
import requests
import urllib2

readfile = open('requiredurls.txt', 'r')
savefile = open('countMemento.txt', 'a')
savefile2 = open('forgraph.txt', 'a')
#inputUrlsList = readfile.readlines()
#readfile.close()

timeMap = re.compile(r'<[^>]+>;rel\w*?=\w*?"timemap".*?')


def nextpage(foundTimeMap):
	
	while len(foundTimeMap) == 1 :
		url = foundTimeMap[0]
		stripedURL = url.strip('<')
		urlStriped = stripedURL.split('>')
		nextPageLink = urlStriped[0]               
		# for the url extracted which has more momento loop it utill we get all
		command = 'curl --silent "'+ nextPageLink + '"'
		response = os.popen(command).read()

		count = response.count('rel="memento"')
		count2 = response.count('rel="first memento"')
		count3 = response.count('rel="last memento"')
		count4 = response.count('rel="memento first"')
		count5 = response.count('rel="memento last"')
		countbig = count + count2 + count3 + count4 + count5             
		foundTimeMap = timeMap.findall(response)   
		
		if countbig != 0:
			return countbig

	return 0
		

for link in readfile:
	command = 'curl --silent "http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/' + link.strip() + '"'
	response = os.popen(command).read()
	#command = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/' + link
	#response = urllib2.urlopen(url=command,timeout=10)
	#time_map = response.read()

	count = response.count('rel="memento"')
	count2 = response.count('rel="first memento"')
	count3 = response.count('rel="last memento"')
	count4 = response.count('rel="memento first"')
	count5 = response.count('rel="memento last"')

	foundTimeMap = timeMap.findall(response)
	returnedcount = nextpage(foundTimeMap)

	finalcount = count + count2 + count3 + count4 + count5 + returnedcount

	output = "{:<10}{}".format(finalcount, link)
	print output

	savefile.write(output)
	savefile2.write(str(finalcount))
	savefile2.write('\n')

