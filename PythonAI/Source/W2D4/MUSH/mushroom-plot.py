# 모듈로딩 --------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import json

# 데이터 변수 선언 --------------------------------------------
DEBUG = True

# --------------------------------------------------
# 데이터 준비
# --------------------------------------------------
# 데이터 가져오기
mushDF = pd.read_csv("../../DATA/MUSH/mushroom.csv", header=None)
print("No Header => ", mushDF.describe())

# 데이터 가공 => 독버섯 & 일반버섯 특징 분류
class_dic = {}
"""


if DEBUG:
    print('mushDF.columns =>', mushDF.columns)
    print('mushDF.indexs =>',  mushDF.index)
    #print("len(mushDF.loc['p'][:]) = {},  len(mushDF.loc['p'][:]) = {}".format(len(mushDF.loc['p'][:]), len(mushDF.loc['e'][:])))
    print(mushDF.iloc[:][:])

for row_index, row in mushDF.iterrows():
    print('row_index =>', row_index)
    print('row =>', row)

    mushClass = row.iloc[0]                                                 # 독버섯 여부 값 라벨데이터 추출
    mushAttr  = row.iloc[1:]                                                # 버섯 속성
    if not (mushClass in class_dic):
        class_dic[mushClass] = row.iloc[1:]
        continue

    for idx, v in enumerate(mushAttr):                                      # 언어별 알파벳 26개 빈도 값 채우기
        #class_dic[mushClass][idx] = (class_dic[mushClass][idx] + v) / 2     # 0~1사이 값으로 범위 한정
        print('v => ', v)


label = []
data = []
for row_index, row in mr.iterrows():
    print('row_index =>', row_index)
    print('row =>', row)
    label.append(row.iloc[0])       # 독버섯 여부 값 라벨데이터 추출
    print('row.iloc[0] =>', row.iloc[0])

    row_data = []
    for v in row.iloc[1:]:
        row_data.append(ord(v))     # 버섯 특징 22가지 문자코드값 변환

    print('row_data =>', row_data)
    data.append(row_data)

for i, lbl in enumerate(freq[0]["labels"]):
    if DEBUG: print('i = {}\t lbl = {}'.format(i, lbl))

    fq = freq[0]["freqs"][i]    # 트레인 용 데이터 추출
    if not (lbl in lang_dic):   # 레이블 언어 데이터 채우기
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):                            # 언어별 알파벳 26개 빈도 값 채우기
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2   # 0~1사이 값으로 범위 한정
"""

# --------------------------------------------------
# 학습
# --------------------------------------------------


# --------------------------------------------------
# 결과 출력
# --------------------------------------------------
# 결과 테스트
