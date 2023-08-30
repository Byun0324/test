from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://news.daum.net/breakingnews/digital")
soup = BeautifulSoup(html, "html.parser")
t=[i for i in range(1,11)]

for j in t:
    news = soup.select("#mArticle > div.box_etc > ul > li:nth-child(1) > div > strong > a")
    n=0

    for new in news:
        url=new.get("href")
        new=new.text.strip()
        if  new !="" :
            n +=1
            print( "{:02d}".format(n), new)
            print( "   ", url)
        