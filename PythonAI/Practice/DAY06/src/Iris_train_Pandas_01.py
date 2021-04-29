import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# csv 데이터 읽어오기
csv = pd.read_csv("../data/iris.csv")

# 필요한 열 추출하기
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]
# print(csv_data)

# 학습용 데이터와 테스트용 데이터 분할
train_data, test_data, train_label, test_label = \
    train_test_split(csv_data,csv_label,test_size=0.3, random_state=42)

# 데이터로 학습하고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기
ac_score = metrics.accuracy_score(test_label,pre)
print("정답률 :",ac_score*100,"%")

