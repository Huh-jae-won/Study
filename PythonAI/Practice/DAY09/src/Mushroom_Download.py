import urllib.request as req
import os.path

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
path = "../data"
name = path+"/mushroom.csv"
if not os.path.exists(path):
    os.mkdir(path)
    print("make dir")

# 파일저장
if not os.path.exists(name):
    req.urlretrieve(url, name)
    print("save ok")
