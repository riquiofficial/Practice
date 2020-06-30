import bs4
import requests

url = ('http://quotes.toscrape.com/random')
res = requests.get(url)
    
soup = bs4.BeautifulSoup(res.text, 'lxml')
quotes = soup.select(".text")
author = soup.select(".author")
for quote in quotes:
	print(quote.text)
for name in author:
    print(name.text)

