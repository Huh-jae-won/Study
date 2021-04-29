'''
공공파일 등은 csv파일이 파일형식이 옛날방식이거나
utf-8형식이 아닐경우가 대다수이다
따라서 알맞은 형식으로 변환이 필요
'''
# 데이터 변수 선언
data_csv = "../data/data.csv"
temp_csv = "../data/tem10y.csv"

# 데이터 준비
# csv파일 읽기
with open(data_csv, "rt") as fr :
    lines = fr.readlines()
# 데이터 추출
lines = ["연,월,일,기온,품질,균질\n"]+lines[5:]   # 헤더제거
print(lines)
lines = map(lambda v:v.replace("/", ","),lines)  # 구분자 제거
result = "".join(lines).strip()                 # 공백 제거
print("new data :")
print(result)

# 새로운 csv파일 생성
with open(temp_csv, "wt",encoding='utf-8') as fw:
    fw.write(result)
    print("save")
