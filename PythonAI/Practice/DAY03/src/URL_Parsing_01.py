import urllib.request
import urllib.parse

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

# 매개변수 URL 인코딩
values = {'stnId':'108'}    # 지역번호

params = urllib.parse.urlencode(values) # 키=값 형태로 인코딩
print("params : ",params)
# 요청 전용 URL 생성
url = API+"?"+params
print("url = ",url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)