#!/usr/bin/env python

from igraph import *

data = load('karate.GraphML')

layout1 = data.layout('circle')
layout2 = data.layout('kk')
plot(data, "beforesplit.pdf", layout=layout1, vertex_label=data.vs['name'])

color = {1: 'red', 2: 'blue'}
plot(data, "aftersplit.pdf", vertex_color = [color[Faction] for Faction in data.vs["Faction"]], layout = layout1, vertex_label=data.vs['name'])

graph3 = data.community_edge_betweenness(clusters=2, weights=data.es['weight'])
cluster2 = graph3.as_clustering()
plot(cluster2, "betweenness2.pdf", vertex_label=data.vs['name'], layout=layout1)

graph4 = data.community_edge_betweenness(clusters=3, weights=data.es['weight'])
cluster3 = graph4.as_clustering()
plot(cluster3, "betweenness3.pdf", vertex_label=data.vs['name'], layout=layout2)

graph5 = data.community_edge_betweenness(clusters=4, weights=data.es['weight'])
cluster4 = graph5.as_clustering()
plot(cluster4, "betweenness4.pdf", vertex_label=data.vs['name'], layout=layout2)

graph6 = data.community_edge_betweenness(clusters=5, weights=data.es['weight'])
cluster5 = graph6.as_clustering()
plot(cluster5, "betweenness5.pdf", vertex_label=data.vs['name'], layout=layout2)

graph7 = data.community_leading_eigenvector(clusters=2, weights=data.es['weight'])
plot(graph7, "eigenvector2.pdf", vertex_label=data.vs['name'], layout=layout1)

plot(data, "aftersplitkk.pdf", vertex_color = [color[Faction] for Faction in data.vs["Faction"]], layout = layout2, vertex_label=data.vs['name'])