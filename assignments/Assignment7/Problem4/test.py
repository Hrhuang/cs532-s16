#!/usr/bin/python
from math import sqrt

def sim_pearson(prefs,p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si]) 
  
  # Sum of the products
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other) 
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]


def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      
      # Flip item and person
      result[item][person]=prefs[person][item]
  return result

def calculateSimilarItems(prefs,movchoice,n=5):
  # Create a dictionary of items showing which other items they
  # are most similar to.
  result={}
  # Invert the preference matrix to be item-centric
  itemPrefs=transformPrefs(prefs)
  choice = movchoice
  
  c=0
  for item in itemPrefs:
    # Status updates for large datasets
    #c+=1
    #if c%100==0: print "%d / %d" % (c,len(itemPrefs))
    # Find the most similar items to this one
    scores=topMatches(itemPrefs,choice,n=n,similarity=sim_pearson)
    result[item]=scores
  return result


movies={}
for line in open('u.item'):
  (id,title)=line.split('|')[0:2]
  movies[id]=title

# Load data
prefs={}
for line in open('u.data'):
  (user,movieid,rating,ts)=line.split('\t')
  prefs.setdefault(user,{})
  prefs[user][movies[movieid]]=float(rating)

movchoice = 'Godfather: Part II, The (1974)'
lestfav = 'Turbo: A Power Rangers Movie (1997)'
remap = transformPrefs(prefs)
love = calculateSimilarItems(prefs,movchoice)
hate = calculateSimilarItems(prefs,lestfav)

print 'The top 5 correlated movies of "Godfather: Part II, The (1974)" are:'
print love
print hate
#print str(top1[0]) + '\n' + str(top1[1]) + '\n' + str(top1[2]) + '\n' + str(top1[3]) + '\n' + str(top1[4]) + '\n'
print 'The bottom 5 correlated movies of "Godfather: Part II, The (1974)" are:'
#print str(least1[0]) + '\n' + str(least1[1]) + '\n' + str(least1[2]) + '\n' + str(least1[3]) + '\n' + str(least1[4]) + '\n'
print 'The top 5 correlated movies of "Turbo: A Power Rangers Movie (1997)" are:'
#print str(top2[0]) + '\n' + str(top2[1]) + '\n' + str(top2[2]) + '\n' + str(top2[3]) + '\n' + str(top2[4]) + '\n'
print 'The bottom 5 correlated movies of "Turbo: A Power Rangers Movie (1997)" are:'
#print str(least2[0]) + '\n' + str(least2[1]) + '\n' + str(least2[2]) + '\n' + str(least2[3]) + '\n' + str(least2[4]) + '\n'

#result = calculateSimilarItems(prefs)
