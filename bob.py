#아침, 점심 저녁 모두 나오는 프로그래밍

from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime

today = str(datetime.date.today())
print("today=",today)

t=today.split("-")   
meal_name=["breakfast","lunch","dinner"]
print("="*50)

for i in meal_name:
    url= f"https://jeju-s.jje.hs.kr/jeju-s/food/{t[0]}/{t[1]}/{t[2]}/{i}" 
    html=urlopen(url)
    soup=BeautifulSoup(html,"html.parser")

    title=soup.select(".food_pop > h2")[0].text 
    title=title.replace("\r","").replace("\n","").replace("\t","")
    print(title)
    

    meal=soup.select("div:nth-child(2) > ul > li:nth-child(2) > dl > dd")
    for m in meal:
        menu=m.text.strip().split(" ")

    for a,b in enumerate(menu,1):
        print( a ,":", b )

    print("="*50)


