from urllib import request
from bs4 import BeautifulSoup

기상청주소 = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
데이터 = request.urlopen(기상청주소)

soup = BeautifulSoup(데이터, "html.parser")

# soup.select()       # 특정 이름을 가진 태그를 모두 찾아줍니다.
# soup.select_one()   # 특정 이름을 가진 태그를 하나만 찾아줍니다.

for location in soup.select("location"):
    도시 = location.select_one("city").string
    for data in location.select("data"):  
        시간 = data.select_one("tmEf").string
        기상상태 = data.select_one("wf").string
        최저기온 = data.select_one("tmn").string
        최고기온 = data.select_one("tmx").string
        print(도시)
        print(시간)
        print(기상상태)
        print(최저기온)
        print(최고기온)