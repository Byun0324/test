from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://news.daum.net/breakingnews/digital")

soup = BeautifulSoup(html, "html.parser")
news = soup.select("#mArticle > div.box_etc > ul > li > div > strong > a")
n=0

for  new in news:
   url=new.get("href")
   new=new.text.strip()
   if  n !=10 :
        n +=1
        print( "{:02d}".format(n), new)
        print( "   ", url)
        