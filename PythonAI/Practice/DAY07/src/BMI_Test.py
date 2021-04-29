from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import joblib


# csv 파일 읽어오기
tbl = pd.read_csv("../data/bmi.csv")

# 열을 자르고 정규화 하기
label = tbl["label"]
w = tbl["weight"]/100   # 최대가 100kg이라고 가정
h = tbl["height"]/200   # 최대가 200cm라고 가정
wh = pd.concat([w,h],axis=1)    # axis설정 안하면 4만행 x 1열로 생성됨

# 학습용과 테스트용 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(wh,label)

# 데이터 학습
clf = svm.SVC()
clf.fit(data_train,label_train)

# 데이터 예측
predict = clf.predict(data_test)

# 결과 테스트
ac_score = metrics.accuracy_score(label_test,predict)
cl_report = metrics.classification_report(label_test,predict)
print("정답률 :",ac_score)
print("리포트 :\n",cl_report)

# 학습 데이터 저장
joblib.dump(clf,"../../DAY08/cgi-bin/bmi.pkl")
print("save-ok")