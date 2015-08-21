#Test of jusText

import requests
import justext

links91 = ['http://nti.org/analysis/articles/mozambique-spring-1989/',
           'http://nti.org/analysis/articles/mozambique-uranium-trade-not-denied/',
           'http://nti.org/analysis/articles/interpol-investigating-report-uranium-market-mozambique/',
           'http://nti.org/analysis/articles/crisis-fallout-soviet-turmoil-ends-nuclear-safety-strategies/',
           'http://nti.org/analysis/articles/radioactive-material-italian-border/',
           'http://nti.org/analysis/articles/uranium-traffic-from-ussr-como-area/',
           'http://nti.org/analysis/articles/nuclear-alarm/',
           'http://nti.org/analysis/articles/new-soviet-nuclear-challenge/',
           'http://nti.org/analysis/articles/soviet-nuclear-yard-sale/',
           'http://nti.org/analysis/articles/explosive-disunion-trade-soviet/',
           'http://nti.org/analysis/articles/nukes-sale/',
           'http://nti.org/analysis/articles/ministry-warns-red-mercury/',
           'http://nti.org/analysis/articles/cia-increase-scruntiny-allies-trade/',
           'http://nti.org/analysis/articles/soviets-said-sell-nuclear-supplies/',
           'http://nti.org/analysis/articles/soviets-reported-sell-materials/']

for link in links91:
    response = requests.get(link)
    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
    for paragraph in paragraphs:
      if not paragraph.is_boilerplate:
          with open("1991.txt", "a") as f:
              f.write(paragraph.text)
              f.write ("\n")
              print "Writing..."
        #print paragraph.text +"\n"
