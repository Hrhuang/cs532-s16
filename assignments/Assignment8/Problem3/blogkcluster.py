import clusters

blognames,words,data=clusters.readfile('blogdata.txt')
def k5():
	(kcluster, t) = clusters.kcluster(data, k=5)
	print "Iteration for k=5 is: " + str(t)

	k=0
	while k < 5:
	  for r in kcluster[k]:
	    print "Centroid " + str(k) + ": " + blognames[r]
	  k+=1
	print "\n"

def k10():
	(kcluster, t) = clusters.kcluster(data, k=10)
	print "Iteration for k=10 is: " + str(t)

	k=0
	while k < 10:
	  for r in kcluster[k]:
	    print "Centroid " + str(k) + ": " + blognames[r]
	  k+=1
	print "\n"

def k20():
	(kcluster, t)= clusters.kcluster(data, k=20)
	print "Iteration for k =20 is: " + str(t)

	k=0
	while k < 20:
	  for r in kcluster[k]:
	    print "Centroid " + str(k) + ": " + blognames[r]
	  k+=1
	print "\n"

k5()
k10()
k20()