#Extract list of links from NTI and save as text file
import requests
import re
from bs4 import BeautifulSoup

smuglink = "http://www.nti.org/analysis/articles/1995-nis-nuclear-trafficking/" #First link I need.
linklist=[]
year = range(1991, 1994)
x=0
while x < len(year):
        link= smuglink[0:37] + str(year[x]) + smuglink[41:]
        linklist.append(link)
        x = x +1

'''#save a copy to disk
with open("ntiyearlinks.txt", "w") as f:
    f.write("\n".join(linklist))'''

#Now loop through the list and save a copy of links on each page


for link in linklist:
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data)
    thelist = []
    corn = soup.findAll(href=re.compile('articles'))
    print corn
    '''for corn in soup.findAll(href=re.compile('articles')):
            found = corn
            thelist.append(found)
            print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"'''




    '''with open("totallinks.txt", "a") as f:
        for corn in soup.findAll(href=re.compile("articles")):
                f.write('href')'''

