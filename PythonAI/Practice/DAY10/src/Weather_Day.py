import pandas as pd
# 일별 평균


# 데이터 변수 선언
temp_csv = "../data/tem10y.csv"
# 데이터 준비
df = pd.read_csv(temp_csv,encoding='utf-8')
# 날짜별 기온 리스트 생성
md = {}
for i, row in df.iterrows():    # i:행번호, row:행의값
    m, d, v = (int(row['월']), int(row['일']), float(row['기온']))
    key = str(m) + '/' + str(d)
    if not(key in md):
        md[key] = []
    md[key] += [v]
print(md)
# 날짜별 기온 평균 계산
avs = {}
print("-------- 날짜별 평균 기온 --------")
for key in md:
    v = avs[key] = sum(md[key]) / len(md[key])
    print("{0} : {1}".format(key,round(v,2)))
