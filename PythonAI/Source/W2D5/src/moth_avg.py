import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager as fm   # 한글 폰트 설정

# 데이터 변수 선언 -------------------------------------
TEMP_CSV = "../../DATA/WEATHER/tem10y.csv"

# ----------------------------------------------------
# 데이터 준비
# ----------------------------------------------------
df = pd.read_csv(TEMP_CSV, encoding="utf-8")

# 월별 평균 구하기
g = df.groupby(['월'])['기온']
gg = g.sum() / g.count()

# ----------------------------------------------------
# 데이터 출력
# ----------------------------------------------------
# 한글 폰트 설정 ---------------------------------------
font_path = r'C:\Windows\Fonts\malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rc('axes', unicode_minus=False)
print(gg)
gg.plot()
plt.savefig("tem-month-avg.png")
plt.show()

