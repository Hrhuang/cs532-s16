#!/usr/local/bin/python

import clusters

(blognames, words, data)=clusters.readfile('blogdata.txt')

daata = clusters.scaledown(data)

clusters.draw2d(daata, blognames, jpeg='MDS.jpg')