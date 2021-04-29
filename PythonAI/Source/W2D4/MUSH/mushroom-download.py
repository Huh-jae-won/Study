# 모듈로딩 ------------------------------------------
import urllib.request as req
import os.path

# 데이터변수 선언 -----------------------------------
SAVE_PATH = '../../DATA/MUSH'
FILE_NAME = SAVE_PATH+'/mushroom.csv'
URL       = 'https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data'

# 폴더 생성
if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)
    print("MAKE DIR OK")

# 파일 저장
if not os.path.exists(FILE_NAME):
    req.urlretrieve(URL, FILE_NAME)
    print("SAVE DATA OK")

print("END DOWNLOAD OK")


