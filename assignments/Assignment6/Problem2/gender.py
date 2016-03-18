import os, sys

readfile = open('mainfollowers.txt', 'r')

for name in readfile:
	command = 'GET https://api.genderize.io/?name=' + name.strip('\n')
	os.popen(command).read()
	#print command