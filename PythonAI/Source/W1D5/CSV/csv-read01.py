# 모듈 로딩 -------------------------------------------
import codecs
import csv

# 데이터 변수 선언 -------------------------------------
file_dir = "C:\\Users\\허재원\\Desktop\\\csv 파일로\\"
filename = ["ChatbotData_사랑.csv", "단발성.csv","연속성.csv"]

try:
    # CSV 파일 읽기 ---------------------------------------
    csv = codecs.open(file_dir+filename[0], "r").read()
    ff = codecs.open(file_dir+"합본.csv","w")
    writer = csv.writer(ff,delimiter=",",quotechar="")
    # CSV 파이썬 리스트로 변환 -------------------------------
    data = []
    rows = csv.split("\r\n")
    for row in rows:
        if row == "": continue
        cells = row.split(",")
        # print(cells)
        data.append(cells)
    print('DATA =>', data)
    # 결과 출력하기 ---------------------------
    for c in data:
        print(c[0], c[1])
except FileNotFoundError:
    print("{} is not exist.".format(file_dir+filename[0]))
finally:
    print("Good-Bye~!")