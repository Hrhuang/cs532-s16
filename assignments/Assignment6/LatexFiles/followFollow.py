import time
import re
import tweepy
from tweepy import OAuthHandler


readfile = open('mainfollowers.txt','r').read().split('\n')
savefile = open('relations.txt', 'a')
savefile2 = open('unauthorized.txt', 'a')

# load my API credentials 

accesstoken = "110800099-ZiXf6imxd24OVqw5nnm4nkHXmVwhX46QQI0Wb3Zt"
accesstokensecret = "FlDFz2Ol035FONaiL9uTzfqRauVArVwwVMuxiHDWQsmwo"
consumerkey = "1N9TkDHB9g4UIbjVj5j6idqnn"
consumersecret = "5Yjw1hRViWd5TloKLmEibPoregSltxO1bY7YJckjnecuSw4n9B"

# create twitter API object

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth, wait_on_rate_limit=True)

i = 0
j = 0

#relation types:
#0: A and B are not following eachother
#1: A is following B
#2: B is following A 
#3: A and B are following eachother
while i < 70:
	try:
		relation = api.show_friendship(source_screen_name = readfile[i], target_screen_name = readfile[j+1])
		if relation[0].following is False and relation[1].following is False:
			print relation[0].screen_name, relation[1].screen_name, 0
			savefile.write(str(relation[0].screen_name))
			savefile.write(',')
			savefile.write(str(relation[1].screen_name))
			savefile.write(',')
			savefile.write(str(0))
		elif relation[0].following is True and relation[1].following is False:
			print relation[0].screen_name, relation[1].screen_name, 1
			savefile.write(str(relation[0].screen_name))
			savefile.write(',')
			savefile.write(str(relation[1].screen_name))
			savefile.write(',')
			savefile.write(str(1))
		elif relation[0].following is False and relation[1].following is True:
			print relation[0].screen_name, relation[1].screen_name, 2
			savefile.write(str(relation[0].screen_name))
			savefile.write(',')
			savefile.write(str(relation[1].screen_name))
			savefile.write(',')
			savefile.write(str(2))
		elif relation[0].following is True and relation[1].following is True:
			print relation[0].screen_name, relation[1].screen_name, 3
			savefile.write(str(relation[0].screen_name))
			savefile.write(',')
			savefile.write(str(relation[1].screen_name))
			savefile.write(',')
			savefile.write(str(3))
		savefile.write('\n')
		j = j+1
		if j == 70:
			i = i+1
			j = i
	except BaseException as e:
		if BaseException is "Failed to send request: ('Connection aborted.', error(SysCallError(104, 'ECONNRESET'),))":
			time.sleep(5)
			continue
		elif BaseException is "Failed to send request: ('Connection aborted.', error(104, 'Connection reset by peer'))":
			time.sleep(5)
			continue
		elif BaseException is "Failed to send request: HTTPSConnectionPool(host='api.twitter.com', port=443): Read timed out. (read timeout=60)":
			time.sleep(5)
			continue
		else:
			print readfile[i], ' ', str(e)
			savefile2.write(str(readfile[i]))
			savefile2.write(' ')
			savefile2.write(str(readfile[j]))
			savefile2.write(' ')
			savefile2.write(str(e))
			savefile2.write('\n')
			j = j+1
			if j == 70:
				i = i+1
				j = i
			continue