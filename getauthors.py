import urllib
import codecs

authors = []

#f = urllib.urlopen("http://www.informatik.uni-trier.de/~ley/db/journals/ws/ws6.html")
f = urllib.urlopen("http://www.informatik.uni-trier.de/~ley/db/conf/www/www2010.html")
s = f.read()
f.close()
soup = BeautifulSoup(s)
allli = soup.findAll( "li")
for li in allli:
   alla = li.findAll('a')
   for a in alla:
     #reenable for testing
     #print a
     author = a.text
     if author:
       authors.append(author)

outfile = codecs.open("authors.txt", "w", "utf-8")
for author in authors:
 outfile.write(author)
outfile.close()
