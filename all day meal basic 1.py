from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime     #오늘 날짜를 불러 올 수 있게 해줌

today = str(datetime.date.today())   # 오늘 날짜를 담음
print("today=",today)
#today="2023-08-01"

t=today.split("-")    # 리스트에 오늘 날자를 연/월/일 별로 나누어 담음
meal_name=["breakfast","lunch","dinner"]
#https://jeju-s.jje.hs.kr/jeju-s/food/2023/08/28/breakfast

for meal in meal_name:
    url= f"https://jeju-s.jje.hs.kr/jeju-s/food/{t[0]}/{t[1]}/{t[2]}/{meal}"   # 리스트 별로 다른 url을 만들 수 있음. 앞에 f 주의
    print(url)
    html=urlopen(url)
    soup=BeautifulSoup(html,"html.parser")
    title=soup.select(".food_pop > h2")[0].text    # 리스트 속 내용물, 그리고 그 중에서도 특수 문자를 제외한 텍스트만 받음
    title=title.replace("\r","").replace("\n","").replace("\t","")   # 리시트를 깔끔하게 정리, 띄어쓰기랑 줄바꾸기 등을 없애줌
    print(title)
