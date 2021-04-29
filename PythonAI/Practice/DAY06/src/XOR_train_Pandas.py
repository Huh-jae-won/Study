import pandas as pd
from sklearn import svm, metrics

# XOR 계산결과 데이터
xor_input = [
    # P, Q, R
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 학습용 데이터와 테스트용 데이터로 분류
xor_df = pd.DataFrame(xor_input)
# xor_df.columns=['a','b','c']
xor_data = xor_df.iloc[:,0:2]   # iloc[행,열 index]
xor_label = xor_df.iloc[:,2]
print("df")
print(xor_df)
print("\ndata")
print(xor_data)
print("\nlabel")
print(xor_label)

# 데이터 학습과 예측
clf = svm.SVC()
clf.fit(xor_data,xor_label)
pre = clf.predict(xor_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(xor_label,pre)
print("정답률 :",ac_score)