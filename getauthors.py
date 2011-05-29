# coding=UTF-8
'''Grabs the list of authors from a DBLP entry. Outputs Unicode authors.txt with
the deduplicated list of authors, one author per line.


Known Issues: Fails on .DS_Store files which Mac Finder may create when copying

Must specify encoding to allow listing authors, try # coding=UTF-8 on first line
'''

import urllib
import codecs
import os
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

#Debugging flag
DEBUG = True

#Specify input
#WHERE = "dir" (i.e. use DIR) or "web" (i.e. use URL)
WHERE = "web"
URL = "http://www.informatik.uni-trier.de/~ley/db/conf/www/www2010.html"
DIR = "tmp2"

#Specify output file
OUTPUT = "authors.txt"

#Message to give the user when complete
MESSAGE = "Output saved in "+OUTPUT

def scrape(authors):
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
	return(authors)

#run on a single file
def grabURL(URL):
	f = urllib.urlopen(URL)
	s = f.read()
	f.close()
	return s
	
#run for the files in a directory
def grabFiles(DIR):
	for f in os.listdir(DIR):
		if DEBUG:
			print os.path.join(os.getcwd(),DIR,f)
			
		infile = codecs.open(os.path.join(os.getcwd(),DIR,f), "r", "utf-8")
		s = infile.read()
		infile.close()
		return s

#@@ todo add SINGLE "file" source as an option to WHERE	
#@@ todo add an array of URLs source as an option to WHERE
if WHERE == "web":
	s = grabURL(URL)
elif WHERE == "dir":
	s = grabFiles(DIR)
else:
	#attempt to fail gracefully
	print("Please specify where to scrape from.")
	exit(0)
	
authors=scrape([])

#deduplicate
#@@ todo maybe better to deduplicate when adding in scrape?
authorset = frozenset(authors)

#sort
deduped_authors = sorted(list(authorset))

#output deduplicated list to a file
outfile = codecs.open(OUTPUT, "w", "utf-8")

for author in deduped_authors:
 if DEBUG:
 	print author
	#\r is carriage return; \n is UNIX linefeed
	outfile.write(author+"\n")

outfile.close()
print MESSAGE