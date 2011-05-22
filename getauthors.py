'''Grabs the list of authors from a DBLP entry. Outputs Unicode authors.txt with
the deduplicated list of authors, one author per line.

Known Issues: Fails on .DS_Store files which Mac Finder may create when copying
'''

import urllib
import codecs
import os
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

DIR = "tmp"
#Debugging flag
DEBUG = True

authors = []

#alternately, run this on a single file
#f = urllib.urlopen("http://www.informatik.uni-trier.de/~ley/db/conf/www/www2010.html")
#s = f.read()
#f.close()

#run for the files in a directory
for f in os.listdir(DIR):
	if DEBUG:
		print os.path.join(os.getcwd(),DIR,f)
	
	infile = codecs.open(os.path.join(os.getcwd(),DIR,f), "r", "utf-8")
	s = infile.read()
	infile.close()
	
	soup = BeautifulSoup(s)
	allli = soup.findAll( "li")
	for li in allli:
	   alla = li.findAll('a')
	   for a in alla:
		 author = a.text
		 if author:
		   #convert HTML entities
		   #via StackOverflow http://stackoverflow.com/questions/701704/how-do-you-convert-html-entities-to-unicode-and-vice-versa-in-python
		   
		   #@@TODO: what's the difference between BeautifulStoneSoup and BeautifulSoup?
	
		   author = unicode(BeautifulStoneSoup(author, convertEntities=BeautifulStoneSoup.HTML_ENTITIES))
		   authors.append(author)

#deduplicate
authorset = frozenset(authors)

#sort
deduped_authors = sorted(list(authorset))

#output deduplicated list to a file
outfile = codecs.open("authors.txt", "w", "utf-8")

for author in deduped_authors:
 if DEBUG:
 	print author
 #@@TODO: what's the difference between \r and \n?	
 outfile.write(author+"\r")

outfile.close()