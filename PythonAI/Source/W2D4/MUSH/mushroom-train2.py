# 모듈 로딩 -------------------------------------------------
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# --------------------------------------------------
# 데이터 준비
# --------------------------------------------------
# 데이터 가져오기
mr = pd.read_csv("../../DATA/MUSH/mushroom.csv", header=None)
# 데이터 내부의 분류 변수 전개하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.iloc[0])                   # 독버섯 & 일반버섯 분류
    print('row.iloc[0] =>', row.iloc[0])

    exdata = []
    for col, v in enumerate(row.iloc[1:]):      # 버섯 22가지 속성 데이터
        if row_index == 0:
            attr = {"dic": {}, "cnt":0}
            attr_list.append(attr)
        else:
            attr = attr_list[col]
        print(row_index, col, 'attr =>', attr)
        print(row_index, col, 'attr_list =>', attr_list)

        # 버섯 특징 기호 저장 최소 2개 ~ 최대 12개
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
            print('v =>', v,  'attr["dic"][v] = ', idx)
        else:
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
            print('idx =>', idx, 'attr["dic"][v] = ', attr["dic"][v])
        d[idx] = 1
        exdata += d
        print(row_index, col, 'd[idx] =>', d[idx])
        print(row_index, col, 'd =>', d, "exdata=>", exdata)
        print(row_index, col, 'attr =>', attr)
        print(row_index, col, 'attr_list =>', attr_list)
        print("\n")
    data.append(exdata)

# --------------------------------------------------
# 학습
# --------------------------------------------------
# 학습 전용과 테스트 전용 데이터 준비
data_train, data_test, label_train, label_test = \
train_test_split(data, label)

# 데이터 학습
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 데이터 예측
predict = clf.predict(data_test)

# --------------------------------------------------
# 결과 출력
# --------------------------------------------------
# 결과 테스트
ac_score = metrics.accuracy_score(label_test, predict)
print("정답률 =", ac_score)
