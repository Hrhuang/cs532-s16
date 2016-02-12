#!/usr/bin/python
import time
from twitter import *

savefile = open('initialurls.txt','a')

# load my API credentials 

accesstoken = "110800099-ZiXf6imxd24OVqw5nnm4nkHXmVwhX46QQI0Wb3Zt"
accesstokensecret = "FlDFz2Ol035FONaiL9uTzfqRauVArVwwVMuxiHDWQsmwo"
consumerkey = "1N9TkDHB9g4UIbjVj5j6idqnn"
consumersecret = "5Yjw1hRViWd5TloKLmEibPoregSltxO1bY7YJckjnecuSw4n9B"

# create twitter API object

auth = OAuth(accesstoken, accesstokensecret, consumerkey, consumersecret)
stream = TwitterStream(auth = auth, secure = True)

# set filter credentials
tweet_iter = stream.statuses.filter(track='sports, game')

for tweet in tweet_iter:

# print URLs found inside
	try:
		for url in tweet["entities"]["urls"]:
			
				print "%s" % url["expanded_url"]
				savefile.write("%s" % url["expanded_url"])
				savefile.write('\n')
				#time.sleep(5)

	except (KeyError, UnicodeEncodeError) as e:
		pass