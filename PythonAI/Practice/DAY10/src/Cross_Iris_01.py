from sklearn import svm, metrics
import random, re

# iris csv 파일 읽어오기
lines = open('../../DAY06/data/iris.csv','r',encoding='utf-8').read().split("\n")
f_tonum = lambda n : float(n) if re.match(r'^[0-9\.]+$',n) else n
f_cols = lambda li : list(map(f_tonum, li.strip().split(',')))
csv = list(map(f_cols,lines))
del csv[0]  # 헤더제거
random.shuffle(csv)
print(csv)
# 데이터를 k개로 분할(k번 교차검증)
k = 5
csvk = [ [] for i in range(k) ]
for i in range(len(csv)):
    csvk[i%k].append(csv[i])

# train용, test용 분리
def split_data_label(rows):
    data = []
    label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return (data,label)

# 정답률 구하기
def calc_score(test,train):
    test_f, test_l = split_data_label(test)
    train_f,train_l = split_data_label(train)
    # 학습시키고 정닫률 구하기
    clf = svm.SVC()
    clf.fit(train_f,train_l)
    predict = clf.predict(test_f)
    return metrics.accuracy_score(test_l,predict)

# k로 분할해서 정답률 구하기
score_list = []
for testc in csvk:
    # testc 이외의 데이터를 훈련용 testc를 test용으로
    trainc = []
    for i in csvk:
        if 1 != testc:
            trainc += i
    sc = calc_score(testc,trainc)
    score_list.append(sc)
print("각각의 정답률 :",score_list)
print("평균 정답률   :",sum(score_list)/len(score_list))