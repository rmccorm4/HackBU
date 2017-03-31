
import requests
from bs4 import BeautifulSoup

baseurl = "http://www.urbandictionary.com/define.php?term="
searchTerm = "binghamton"
#searchTerm = input() #to take any word from input

fullurl = baseurl+searchTerm

request = requests.get(fullurl)

html = request.content
#just html returns a lot of garbage and stuff you're not looking for, so we use
#beautiful soup

#inspect element for phrases you're looking for
#check out the div class name
#on urban dictionary the div class is called meaning (css class)

#tell beautifulsoup to look for class "meaning"

soup = BeautifulSoup(html, "html.parser")

div=soup.find(class_="meaning")
definition = div.text
print(definition)

#MOBILE VERSIONS OF WEBSITES ARE MUCH EASIER TO SCRAPE, THEY HAVE A LOT LESS CRAP

#Selenium lets you control chrome, look into this
#Selenium is a mixture of requests and beautiful soup, it basically lets you
#simulate clicks in a browser

#Look into "IPython"? Interactive python?

url = ""

imageurl = div.attrs["src"]
response = requests.get(imageurl)

myfile = open("imagewoo", "wb")
for byte in response:
myfile.write(byte)
