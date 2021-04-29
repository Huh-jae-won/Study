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
print("No Header => ", mr)

# 데이터 가공
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
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)