import json

data={
'data':'2020-02-08',
'price':{
    'apple':500,
    'banana':2500
    },
'store':'현백'
}
savename = "../data/jdata.json"

# json형식으로
jdata = json.dumps(data)    # 파이썬객체를 json형태로 변환

# json파일로 저장
with open(savename,"w",encoding="utf-8") as fp :
    fp.write(jdata)

