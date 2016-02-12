
gett = open('urlsRoundV2.txt', 'r')
savefile = open('unqiueurls.txt', 'a')
savefile2 = open('requiredurls.txt', 'a')

#set function remove duplicates in a list
unqiue = set(gett)
for link in unqiue:
	#print link
	savefile.write(link)

#get the top 1000 strings
with open('unqiueurls.txt', 'r') as unqiueurls:
	top1000 = [next(unqiueurls) for x in xrange(1000)]
for links in top1000:
	savefile2.write(links)


#i = 0

#def forloops(unqiue, i):
	#for link in unqiue:
		#i = i + 1
		#print link
		#savefile.write(link)
		#return i
	

#while i < 1000:
	#i = forloops(unqiue, i)
		
