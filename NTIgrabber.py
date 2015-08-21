## NTI page extractor

## Goes through NTI smuggling pages to pull out all reports by year and puts them
## into a spreadsheet for further analysis

##  First I need to build the page list, so I'll try to get python to help
##  All the pages follow the same pattern, only differing in year, so...

smuglink = "http://www.nti.org/analysis/articles/1995-nis-nuclear-trafficking/" #First link I need.
linklist=[]
year = range(1991, 2012)
x=0
while x < len(year):
        link= smuglink[0:37] + str(year[x]) + smuglink[41:]
        linklist.append(link)
        x = x +1
#print linklist

##Now I've got all the links to all the year pages 

##  Next, I've got to get the article links from each of the year pages

import requests
import re
from bs4 import BeautifulSoup

r  = requests.get(linklist[0])

data = r.text

soup = BeautifulSoup(data)

###  Found this code (after HOURS of searching) to do the simple task of
### pulling out a link that matches a certain pattern, e.g. nti.org/analysis/articles
### print (soup.findAll(href=re.compile("articles")))

## Now I need to extract all the links that match the NTI article pattern and put them in a list
linklist2 = []
for link in soup.findAll(href=re.compile("articles")):
    link1 = [link.get('href')]
    linklist2.append(link1)
    #print(link.get('href'))


print linklist2
## So, right now I can print all the links on the page
## I still need to figure out how to make them into urls that can be used to get the text I want to read
## and I don't know yet how to put these into a list the proper way.



#import urllib2
#import re

#connect to a URL
#website = urllib2.urlopen(linklist[0])

#read html code
#html = website.read()

#use re.findall to get all the links
#pattern= "http://www.nti.org/analysis/articles/[A-Za-z0-9.]"
#links = re.search(pattern, html)

#links.group()





 
