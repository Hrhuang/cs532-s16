import os, sys

#readfile = open('requiredurls.txt', 'r')
directory = '/home/hhuang/Documents/CS532/WebScienceAssig/Assignment10/Problem4/Raw/RawFiles/'
count = 0

for filename in os.listdir(directory):
	count = count + 1
	#hashmd5sum = 'echo -n ' + line.strip() + ' | md5sum'
	#hashresult = os.popen(hashmd5sum).read()
	command = 'lynx -dump -force_html "' + directory + filename + '" > "'+ filename + '"'
	os.popen(command).read()
	#print command