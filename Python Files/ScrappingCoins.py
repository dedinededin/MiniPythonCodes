from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://coinmarketcap.com/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"col-xs-12"})
coins =containers[1].findAll("tr")
itercoins= iter(coins)
next(itercoins)
for coin in itercoins:
    name=coin.find("a").text
    x = coin.findAll("td",{"class":"no-wrap text-right"})
    y= x[0].text
    print (name+":"+y)








