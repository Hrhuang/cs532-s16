import feedparser
import re
import math
import docclass

savefile = open("data.txt", "a")

# Takes a filename or URL of a blog feed and classifies the entries
def read(feed,classifier):

  splitRegexp = re.compile( r"<[^>]+>" )

  num=0
  # Get feed entries and loop over them
  f=feedparser.parse(feed)

  string1 = '-------------------------------- Manually classify first 50 entries --------------------------------\n'
  dividline = "_" * 100 + "\n"
  print string1
  savefile.write(string1)
  string2 = "{:<60}{:<12}{:<10}{:<8}{:<10}{}".format("Title", "Prediction", "Actual", 'cprob', 'fisherprob',"\n")
  print string2
  savefile.write(string2)
  savefile.write(dividline)

  for entry in f['entries'][0:50]:
    num=num +1
    # Print the contents of the entry
    title=entry['title'].encode('utf-8').replace("'","")
    print 'Title:     '+ title
    
    summary = splitRegexp.sub( "", entry[ "summary" ] )
    
    print summary #entry['summary'].encode('utf-8')

    # Combine all the text to create one item for the classifier
    #fulltext='%s\n%s\n%s' % (entry['title'],entry['publisher'],entry['summary'])
    fulltext='%s\n%s' % (entry['title'],entry['summary'])
    # Remove apostrophes
    fulltext=fulltext.replace("'","")
    # Print the best guess at the current category
    predicted=str(classifier.classify(fulltext))
    print 'Predicted category: ', predicted

    # Ask the user to specify the correct category and train on that
    actual=raw_input('Actual category: ')
    classifier.train(fulltext, actual)

    feature=raw_input('Enter string classifier: ')

    #classifier.train(entry,cl)
    # probability the item should be in this category
    cp=round(classifier.cprob(feature,predicted),4)
    fcp=round(classifier.fisherprob(feature,predicted),4)
    print 'cprob: ', str(cp)
    print 'fisherprob: ', str(fcp)
    string3 = "{:<60}{:<12}{:<10}{:<8}{:<10}{}".format(title, predicted, actual, str(cp), str(fcp), "\n")
    savefile.write(string3)
 
    # Save the manual classifications
    # num, entry, feature, predicted, actual, cprob=None
    classifier.manualClassdb(num, title, feature, predicted, actual, cp, fcp)
  savefile.write(dividline)
#def autoClassify(feed,classifier):
  num=50
  string4 = '\n---------------------------- Other 50 automaticly classified entries -------------------------------\n'
  print string4
  savefile.write(string4)
  savefile.write(string2)
  savefile.write(dividline)
  # Get feed entries and loop over them
  #f=feedparser.parse(feed)
  for entry in f['entries'][50:100]:
    num=num+1
    # Print the contents of the entry
    title=entry['title'].encode('utf-8').replace("'","")
    print 'Title:     '+ title
    summary = splitRegexp.sub( "", entry[ "summary" ] )
    
    print summary #entry['summary'].encode('utf-8')

    # Combine all the text to create one item for the classifier
    #fulltext='%s\n%s\n%s' % (entry['title'],entry['publisher'],entry['summary'])
    fulltext='%s\n%s' % (entry['title'],entry['summary'])
    fulltext=fulltext.replace("'","")
    # Print the best guess at the current category
    predicted=str(classifier.classify(fulltext))
    print 'Predicted: ', predicted

    # Ask the user to specify the correct category
    actual=raw_input('Actual category: ')
    feature=raw_input('Enter string classifier: ')

    
    # probability the item should be in this category
    cp=round(classifier.cprob(feature,predicted),4)
    fcp=round(classifier.fisherprob(feature,predicted),4)
    print 'cprob: ', str(cp)
    print 'fisherprob: ', str(fcp)

    string6 = "{:<60}{:<12}{:<10}{:<8}{:<10}{}".format(title, predicted, actual, str(cp), str(fcp), "\n")
    savefile.write(string6)
    # Save the trained classifications
    # num, entry, feature, predicted, cprob(feature, predicted)
    classifier.autoClassdb(num, title, feature, predicted, actual, cp, fcp)    
  #return classifier
  savefile.write(dividline)

def entryfeatures(entry):
  splitter=re.compile('\\W*')
  f={}
  
  # Extract the title words and annotate
  titlewords=[s.lower() for s in splitter.split(entry['title']) 
          if len(s)>2 and len(s)<20]
  for w in titlewords: f['Title:'+w]=1
  
  # Extract the summary words
  summarywords=[s.lower() for s in splitter.split(entry['summary']) 
          if len(s)>2 and len(s)<20]

  # Count uppercase words
  uc=0
  for i in range(len(summarywords)):
    w=summarywords[i]
    f[w]=1
    if w.isupper(): uc+=1
    
    # Get word pairs in summary as features
    if i<len(summarywords)-1:
      twowords=' '.join(summarywords[i:i+1])
      f[twowords]=1
    
  # Removed: Keep creator and publisher whole
  #f['Publisher:'+entry['publisher']]=1

  # UPPERCASE is a virtual word flagging too much shouting  
  if float(uc)/len(summarywords)>0.3: f['UPPERCASE']=1
  
  return f


cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('psMovies.db')
read('psMovies.xml',cl)
  
