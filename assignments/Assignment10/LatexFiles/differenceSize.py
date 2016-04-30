import os, sys

savefile = open('newProcessedSizes.txt', 'a')
path = "/home/hhuang/Documents/CS532/WebScienceAssig/Assignment10/Problem4/Processed/ProcessedFiles/"

for filename in os.listdir(path):
	filepath = os.path.join(path, filename)
	size = os.path.getsize(filepath)
	savefile.write(str(size))
	savefile.write('\n')
	print size
