import os, sys

#readfile = open('requiredurls.txt', 'r')
directory = '/mnt/hgfs/SchoolWork/WebScience/Assignments/HW3/Problem1/RawHTMLs/rawHTMLs/'
count = 0

for filename in os.listdir(directory):
	count = count + 1
	#hashmd5sum = 'echo -n ' + line.strip() + ' | md5sum'
	#hashresult = os.popen(hashmd5sum).read()
	command = 'lynx -dump -force_html "' + directory + filename + '" > "'+ filename + '"'
	os.popen(command).read()
	#print command