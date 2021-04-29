import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

wine_csv = "../data/wine.csv"

wine  = pd.read_csv(wine_csv, sep=";", encoding="utf-8")

# 데이터를 레이블,데이터로 분리
y = wine["quality"]
x = wine.drop("quality",axis=1) # axis : 행방향, 열방향


# y레이블 변경
newlist = []
for v in list(y):
    if v<=4 :
        newlist +=[0]
    elif v<=7 :
        newlist +=[1]
    else:
        newlist +=[2]
y = newlist
print(y)

# 학습용, 테스트용 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

# 학습
model = RandomForestClassifier()
model.fit(x_train,y_train)

# 예측
predict = model.predict(x_test)
print("정답률 :",accuracy_score(y_test,predict))
print("리포트 :\n",classification_report(y_test,predict))