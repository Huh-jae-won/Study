import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# 데이터 읽어오기
mr = pd.read_csv("../data/mushroom.csv", header=None)   # 헤더를 인덱스로 바꿈
# 데이터 내부의 분류 변수 전개하기
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.iloc[0])   # 독버섯, 일반버섯 분류
    # 각행의 0번 열은 독 or 일반 확인 가능
    exdata = []
    for col, v in enumerate(row[1:]):
        if row_index == 0 :
            attr = {"dic":{},"cnt":0}
            attr_list.append(attr)
        else :
            attr = attr_list[col]
        # 버섯 특징 기호 저장 최소2개 ~ 최대12개
        d = [0,0,0,0,0,0,0,0,0,0,0,0]
        if v in attr["dic"]:
            idx = attr["dic"][v]
        else :
            idx = attr["cnt"]
            attr["dic"][v] = idx
            attr["cnt"] += 1
        d[idx] = 1
        exdata += d
    data.append(exdata)

# 학습용 데이터용 분류
data_train, data_test, label_train, label_test = train_test_split(data, label)

# 데이터 학습
clf = RandomForestClassifier()
clf.fit(data_train,label_train)

# 데이터 예측
predict = clf.predict(data_test)

# 결과 테스트
ac_score = metrics.accuracy_score(label_test,predict)
cl_report = metrics.classification_report(label_test,predict)
print("정답률 :",ac_score)
print("리포트 :")
print(cl_report)

