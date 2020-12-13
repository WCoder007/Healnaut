from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.webmd.com/search/search_results/default.aspx?query=headache"
req = Request(url, headers={'User-Agent': 'Mozilla/5.e'})

#Get the web page
webpage = urlopen(req).read()

page_soup = soup(webpage,"html.parser")
#print(page_soup.prettify())

title = page_soup.find("b")
print(title)
containers = page_soup.findAll("p","search-results-doc-description")
for container in containers:
    print(container.text.strip(), end='\n') 