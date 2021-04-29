import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager as fm   # 한글폰트설정

# 데이터 변수 선언
temp_csv = "../data/tem10y.csv"
# 데이터 준비
df = pd.read_csv(temp_csv,encoding='utf-8')

# 월별 평균 구하기
g = df.groupby(['월'])['기온']   
gg = g.sum() / g.count()
# gg =df.groupby('월')['기온'].mean()와 위과정은 같음
'''
df.groupby('월') : 월
df.query('월'=='3') : 월이 3인것들만 모아둠
'''
# 데이터 출력
font_path = r'C:\Windows\Fonts\malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rc('axes', unicode_minus=False)
print(gg)
gg.plot()
plt.title("tem-month-avg.png")
plt.savefig("tem-month-avg.png")
plt.show()