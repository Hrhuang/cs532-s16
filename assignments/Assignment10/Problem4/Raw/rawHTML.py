import os, sys

readfile = open('requiredurls.txt', 'r')
savefile = open('fileNumWithLink.txt', 'a')
count = 0

for line in readfile:
	count = count + 1
	#hashmd5sum = 'echo -n ' + line.strip() + ' | md5sum'
	#hashresult = os.popen(hashmd5sum).read()
	filenames = str(count) + '.txt"'
	command = 'curl -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0)Gecko/20100101 Firefox/44.0" "' + line.strip() + '" > "'+ filenames
	os.popen(command).read()
	numberlink = "{:<10}{}".format(filenames[:-1], line)
	savefile.write(numberlink)
	#print command
	#print hashresult