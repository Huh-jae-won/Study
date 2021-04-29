import requests
import json

# API키
api_key = "03777ecfcddee50ac794952ba652ff2a"

# 날씨를 확인할 도시
cities = ["Seoul,KR","Tokyo,JP","New York,US"]

# API 지정
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 절대온도 -> 섭씨
k2c = lambda k: k-273.15

# 각 도시의 정보 추출
for name in cities:
    # print(name)
    # API의 URL 구성하기
    url = api.format(city=name,key=api_key)
    # API에 요청을 보내 데이터 추출하기
    r = requests.get(url)
    # 결과를 Json형식으로 변환
    data = json.loads(r.text)
    # 결과 출력
    print("+ 도시 : ",data["name"])
    print("| 날씨 : ",data["weather"][0]["description"])
    print("| 최저 기온 : ",k2c(data["main"]["temp_min"]))
    print("| 최고 기온 : ", k2c(data["main"]["temp_max"]))
    print("| 습도 : ",data["main"]["humidity"])
    print("| 기압 : ",data["main"]["pressure"])
    print("| 풍향 : ",data["wind"]["deg"])
    print("| 풍속 : ",data["wind"]["speed"])
    print()