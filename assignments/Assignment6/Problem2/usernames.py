import time
import re
import tweepy
from tweepy import OAuthHandler

readfile = open('mainfollowers.txt','r')
savefile = open('twitterNames.txt', 'a')

# load my API credentials 

accesstoken = "110800099-ZiXf6imxd24OVqw5nnm4nkHXmVwhX46QQI0Wb3Zt"
accesstokensecret = "FlDFz2Ol035FONaiL9uTzfqRauVArVwwVMuxiHDWQsmwo"
consumerkey = "1N9TkDHB9g4UIbjVj5j6idqnn"
consumersecret = "5Yjw1hRViWd5TloKLmEibPoregSltxO1bY7YJckjnecuSw4n9B"

# create twitter API object

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)

api = tweepy.API(auth)

for line in readfile:
	user = api.get_user(line)
	name = user.name
	print line, name
	savefile.write(str(name))
	savefile.write('\n')