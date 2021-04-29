from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 변수 선언 -------------------------------------
TEMP_CSV = "../../DATA/WEATHER/tem10y.csv"

# ----------------------------------------------------
# 함수
# ----------------------------------------------------
# 과거 6일 데이터 기반으로 학습 데이터 생성 함수
def make_data(data):
    x = []                          # 학습 데이터
    y = []                          # 결과
    interval = 6                    # 6일 단위
    temps = list(data["기온"])

    for i in range(len(temps)):
        if i < interval: continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(temps[d])
        x.append(xa)
    return (x, y)

# ----------------------------------------------------
# 데이터 준비
# ----------------------------------------------------
df = pd.read_csv(TEMP_CSV, encoding="utf-8")

#  학습 전용과 테스트 전용 분리
train_year = (df["연"] <= 2015)
test_year  = (df["연"] >= 2016)

# 학습용 & 검증용 데이터 분리
train_x, train_y = make_data(df[train_year])
test_x, test_y   = make_data(df[test_year])

# ----------------------------------------------------
# 학습
# ----------------------------------------------------
lr = LinearRegression(normalize=True)
lr.fit(train_x, train_y)
pre_y = lr.predict(test_x)

# 결과 평가
diff_y=abs(pre_y - test_y)
print('average=', sum(diff_y)/len(diff_y))   # 오차 평균
print('max=', max(diff_y))                   # 최대값

# ----------------------------------------------------
# 출력
# ----------------------------------------------------
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(test_y, c='r')
plt.plot(pre_y, c='b')
plt.savefig('tenki-kion-lr.png')
plt.show()

