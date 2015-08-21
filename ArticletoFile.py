#Script to save NTI news abstracts to file

import requests
import justext

with open("wtf.txt", "rb") as f: #use file where saved yearly links are stored
    mylist = [line.rstrip("\n").rstrip("\r") for line in f]


for link in mylist:
    response = requests.get(link)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    #print paragraphs
    for paragraph in paragraphs:
      if not paragraph.is_boilerplate:
          #print paragraph
          with open("1995.txt", "a") as f: #save file with name of link year
              f.write(paragraph.text)
              f.write ("\n")
              print "Writing..."  

