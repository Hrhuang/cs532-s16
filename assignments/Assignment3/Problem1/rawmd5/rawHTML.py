import os, sys

readfile = open('requiredurls.txt', 'r')
count = 0

for line in readfile:
	count = count + 1
	hashmd5sum = 'echo -n ' + line.strip() + ' | md5sum'
	hashresult = os.popen(hashmd5sum).read()
	command = 'curl -L "' + line.strip() + '" > "'+ str(count) + '_' + hashresult.strip().replace(' ', '').replace('-', '')  + '.html"'
	os.popen(command).read()
	#print command
	