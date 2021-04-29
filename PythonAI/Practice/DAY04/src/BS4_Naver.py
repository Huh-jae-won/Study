from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

# 데이터를 가져옴
res = req.urlopen(url)

# 데이터를 추출하기 위해 추출가능한 형태로 바꿔줌
soup = BeautifulSoup(res,'html.parser')

# 달러,엔화 환율
#exchangeList > li.on > a.head.usd > div > span.value
#exchangeList > li:nth-child(2) > a.head.jpy > div > span.value

usd = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
jpy = soup.select_one("#exchangeList > li:nth-child(2) > a.head.jpy > div > span.value")
print("달러 환율 : ", usd.get_text())
print("엔화 환율 : ", jpy.string)        # str형