from sklearn import svm
import joblib
import json

# 각언어의 출현빈도 데이터 읽어 들이기
with open("../data/freq.json",'r',encoding='utf-8') as fp :
     d = json.load(fp)
     data = d[0]

# 데이터 학습
clf = svm.SVC()
clf.fit(data["freqs"],data["labels"])

# 학습 데이터 저장
joblib.dump(clf,"../data/freq.pkl")
print("ok")