#! /usr/bin/python

import numpredict

vecs = {}

f = open("blogdata.txt", "r")

for line in f:
	a = line.strip('\n').split('\t');
	b = a.pop(0)
	vecs[b] = a
	

fm = 'F-Measure'
ws = 'Web Science and Digital Libraries Research Group'

a = vecs[fm]
temp = vecs.values()
temp.pop(vecs.keys().index(fm))

a = numpredict.knnestimate(temp,a,k=5)


k = [1, 2, 5, 10, 20]
print "K Nearest Neighbors for F-Measure:"
for i in k:
  print "When k = "+str(i)
  for j in range(i):
    b = a[j][1]
    print vecs.keys()[b]
print '\n'

a = vecs[ws]
temp = vecs.values()
temp.pop(vecs.keys().index(ws))

a = numpredict.knnestimate(temp,a,k=5)

print "K Nearest Neighbors for WS-DL:"
for i in k:
  print "When k = "+str(i)
  for j in range(i):
    b = a[j][1]
    print vecs.keys()[b]    
