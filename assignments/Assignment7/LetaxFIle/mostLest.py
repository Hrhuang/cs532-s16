
readfile = open('u.data', 'r')
readfile2 = open('u.item', 'r')
#savefile = open('mostLest.txt', 'a')
data = readfile.readlines()
data2 = readfile2.readlines()

substitutes = ['286', '429', '484']
most = []
lest = []
favtitles1 = []
favtitles2 = []
favtitles3 = []
hatetitles1 = []
hatetitles2 = []
hatetitles3 = []
def favorites(item):
	most =[]
	for line in data:
		(userid, itemid, rating, timestamp) = line.split('	')
		if userid == item and rating == '5':
			most.append((userid, itemid, rating))
	return most

def lestfav(item):
	lest =[]
	for line in data:
		(userid, itemid, rating, timestamp) = line.split('	')
		if userid == item and rating == '1':
			lest.append((userid, itemid, rating))
	return lest

def movies(mvid):
	for line in data2:
		(movieid, movietitle, releasedate, videodate, IMDBURL, unknown, action, adventure, animation, children, comedy, crime, docu, drama, fantasy, filenoir, horror, musical, mystery, romance, scifi, thriller, war, western) = line.split('|')
		if movieid == mvid:
			return movietitle

for item in substitutes:
	most.append(favorites(item))
for item in substitutes:
	lest.append(lestfav(item))
subfav1 = most[0][0][1], most[0][1][1], most [0][2][1]
subfav2 = most[1][0][1], most[1][1][1], most [1][2][1]
subfav3 = most[2][0][1], most[2][1][1], most [2][2][1]
sublest1 = lest[0][0][1], lest[0][1][1], lest [0][2][1]
sublest2 = lest[1][0][1], lest[1][1][1], lest [1][2][1]
sublest3 = lest[2][0][1], lest[2][1][1], lest [2][2][1]
for mvid in subfav1:
	favtitles1.append(movies(mvid))
for mvid in subfav2:
	favtitles2.append(movies(mvid))
for mvid in subfav3:
	favtitles3.append(movies(mvid))
for mvid in sublest1:
	hatetitles1.append(movies(mvid))
for mvid in sublest2:
	hatetitles2.append(movies(mvid))
for mvid in sublest3:
	hatetitles3.append(movies(mvid))

print 'The favorite 3 movies of user ' + substitutes[0] + ' are:'
print favtitles1[0] + '\n' + favtitles1[1] + '\n' + favtitles1[2] + '\n'
print 'The 3 lest favorite movies of user ' + substitutes[0] + ' are:'
print hatetitles1[0] + '\n' + hatetitles1[1] + '\n' + hatetitles1[2] + '\n'
print 'The favorite 3 movies of user ' + substitutes[1] + ' are:'
print favtitles2[0] + '\n' + favtitles2[1] + '\n' + favtitles2[2] + '\n'
print 'The 3 lest favorite movies of user ' + substitutes[1] + ' are:'
print hatetitles2[0] + '\n' + hatetitles2[1] + '\n' + hatetitles2[2] + '\n'
print 'The favorite 3 movies of user ' + substitutes[2] + ' are:'
print favtitles3[0] + '\n' + favtitles3[1] + '\n' + favtitles3[2] + '\n'
print 'The 3 lest favorite movies of user ' + substitutes[2] + ' are:'
print hatetitles3[0] + '\n' + hatetitles3[1] + '\n' + hatetitles3[2] + '\n'
