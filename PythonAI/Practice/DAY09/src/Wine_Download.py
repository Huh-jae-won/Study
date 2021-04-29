from urllib import request as req
import os
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
path = "../data"

# 데이터 준비
if not os.path.exists(path):
    os.makedirs(path)

# 다운로드
csv = path+"/winequality-white.csv"
req.urlretrieve(url,csv)