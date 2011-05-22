'''Grabs the list of authors from a DBLP entry. Outputs Unicode authors.txt with
the deduplicated list of authors, one author per line.'''

import urllib
import codecs
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

#Debugging flag
DEBUG = False

authors = []

f = urllib.urlopen("http://www.informatik.uni-trier.de/~ley/db/conf/www/www2010.html")
s = f.read()
f.close()
soup = BeautifulSoup(s)
allli = soup.findAll( "li")
for li in allli:
   alla = li.findAll('a')
   for a in alla:
     author = a.text
     if author:
       #convert HTML entities
       #via StackOverflow http://stackoverflow.com/questions/701704/how-do-you-convert-html-entities-to-unicode-and-vice-versa-in-python
       author = unicode(BeautifulSoup(author, convertEntities=BeautifulSoup.HTML_ENTITIES))
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
 outfile.write(author+"\r")

outfile.close()