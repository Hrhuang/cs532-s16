#!/usr/bin/python
import time
import tweepy
from tweepy import OAuthHandler


savefile = open('mainfollowers.txt','a')

# load my API credentials 

accesstoken = "110800099-ZiXf6imxd24OVqw5nnm4nkHXmVwhX46QQI0Wb3Zt"
accesstokensecret = "FlDFz2Ol035FONaiL9uTzfqRauVArVwwVMuxiHDWQsmwo"
consumerkey = "1N9TkDHB9g4UIbjVj5j6idqnn"
consumersecret = "5Yjw1hRViWd5TloKLmEibPoregSltxO1bY7YJckjnecuSw4n9B"

# create twitter API object

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)


api = tweepy.API(auth, wait_on_rate_limit=True)
mainuser = api.get_user('jcdl2012')
userName = mainuser.screen_name
#followersCounts = mainuser.followers_count
print userName
savefile.write(userName)
savefile.write('\n')

users = tweepy.Cursor(api.followers, userName, count=200).items()

for follower in users:
	try:
		#fcount = follower.followers_count
		fname = follower.screen_name
		print fname
		savefile.write(fname)
		savefile.write('\n')
	except tweepy.error.RateLimitError:
		monitor_rate_limit=True, wait_on_rate_limit=True
		continue
	except StopIteration:
		break

    