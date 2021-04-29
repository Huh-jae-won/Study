import pandas as pd
from sklearn import model_selection, svm, metrics
from sklearn.model_selection import GridSearchCV

# MNIST 학습데이터 읽어오기
train_csv = pd.read_csv("../../DAY07/data/mnist/train.csv")
test_csv = pd.read_csv("../../DAY07/data/mnist/t10k.csv")

# 필요한 열 추출
train_label = train_csv.iloc[:,0]
train_data = train_csv.iloc[:,1:577]
test_label = test_csv.iloc[:,0]
test_data = test_csv.iloc[:,1:577]
print("학습데이터의 수 :",len(train_label))

# 그리드 서치 매개변수 설정
params = [
    {"C":[1,10,100,1000], "kernel":["linear"]},                     # 선형 방식
    {"C":[1,10,100,1000], "kernel":["rbf"], "gamma":[0.001,0.0001]} # 
]
# 그리드 서치 수행
clf = GridSearchCV(svm.SVC(),params,n_jobs=-1)
# n_jobs : 병렬계산할 프로세스 수 지정, -1: 알아서
clf.fit(train_data,train_label)
print("학습기 :",clf.best_estimator_)

# 테스트 데이터 확인
predict = clf.predict(test_data)
ac_score = metrics.accuracy_score(test_label,predict)
print("정답률 :",ac_score)