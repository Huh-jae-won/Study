from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# 데이터변수 선언
temp_csv = "../data/tem10y.csv"

# 과거 6일 데이터 기반으로 학습용,정답 분리하는 함수
def make_data(data):
    x = []          # 학습 데이터
    y = []          # 결과
    interval = 6    # 6일
    temps = list(data["기온"])    # 기온만 쭉 들어감
    for i in range(len(temps)):
        if i < interval:
            continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i+p-interval    # i이전 6일간의 데이터 인덱스
            xa.append(temps[d])
        x.append(xa)
    return(x,y)

# 데이터 준비
df = pd.read_csv(temp_csv,encoding='utf-8')

# 학습용 테스트용 분리
train_year = (df["연"]<=2015)
test_year = (df["연"]>2015)

# 학습용 & 정답용 데이터 분리
train_x, train_y = make_data(df[train_year])
test_x, test_y = make_data(df[test_year])

# 학습
lr = LinearRegression(normalize=True)
lr.fit(train_x,train_y)
pre_y = lr.predict(test_x)

# 결과
diff_y = abs(pre_y - test_y)    # 예측 - 실측
print("avg :",sum(diff_y)/len(diff_y))
print("max :",max(diff_y))

# 출력
plt.figure(figsize=(10,6),dpi=100)
plt.plot(test_y,c='r')
plt.plot(pre_y,c='b')
plt.savefig('../data/tenki-kion-lr.png')
plt.show()