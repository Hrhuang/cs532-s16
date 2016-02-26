from pygraphml import Graph
from pygraphml import GraphMLParser
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

savefile = open('faceFriendCount.txt', 'a')

parser = GraphMLParser()
g = parser.parse("mln.graphml")

nodes = g.nodes()
count = 0

for node in nodes:
	count = count + 1
	try:
		friendName = node['name']
		friendCount = node['friend_count']
		print friendCount, friendName
		savefile.write('{},{}'.format(friendCount, friendName))
		savefile.write('\n')
	except KeyError:
		pass

mainUserName = "Michael L. Nelson"
print count, mainUserName
savefile.write('{},{}'.format(count, mainUserName))