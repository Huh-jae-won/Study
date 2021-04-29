from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "../data/forecast.xml"

# web데이터 다운로드 후 파일 저장
if not os.path.exists(savename):
    req.urlretrieve(url,savename) # 경로가 없으면 생성하여 저장

# web데이터 분석
xml = open(savename,mode="r",encoding="utf-8").read()
soup = BeautifulSoup(xml,"html.parser")
info = {}
for location in soup.find_all("location"):
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

# 각 지영의 날씨를 구분해서 출력
for weather in info.keys():
    print("+",weather)
    for name in info[weather]:
        print("|-", name)
    print()