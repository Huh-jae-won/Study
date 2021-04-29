import urllib.request as req
import os.path
import json

url = "https://api.github.com/repositories"
savename = "../data/repo.json"
# web데이터 json파일 다운로드
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

# JSON파일 분석
js = open(savename,"r", encoding="utf-8").read()

items = json.loads(js)  # 파이썬 객체로 변환
for i in items:
    print("%-22s"%i["name"],":",i["owner"]["login"])

