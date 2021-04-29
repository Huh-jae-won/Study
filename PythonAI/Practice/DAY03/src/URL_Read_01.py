import urllib.request

url = 'http://api.aoikujira.com/ip/ini'
res = urllib.request.urlopen(url)
data = res.read()
print("data 타입 : ",type(data))
# 받아온 형식은 바이너리 형식

# 바이너리를 문자열로 변환
text = data.decode("utf-8")
print(text)