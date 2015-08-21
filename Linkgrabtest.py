#Use to get all the links from the NTI NIS trafficking pages and save them as
#separate files by year.  

import re
import linkGrabber


links = linkGrabber.Links("http://www.nti.org/analysis/articles/1995-nis-nuclear-trafficking/")

#open the file containing the main page link list
with open("ntiyearlinks.txt", "rb") as x:
    ntilinks = [line.rstrip("\n").rstrip("\r") for line in x]

#start a counter to name files
z = 0

#hand each link over to the link grabber
for item in ntilinks:
    link = linkGrabber.Links(item)
    data = link.find(href=re.compile("articles"))
    filename = "year" + str(z) + ".txt"
    for link in data:
        with open(filename, "a") as f:
            f.write("http://nti.org")
            f.write(link.get('href'))
            f.write("\n")
    z +=1 


            

