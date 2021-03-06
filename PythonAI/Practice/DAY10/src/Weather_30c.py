import matplotlib.pyplot as plt
from matplotlib import font_manager as fm   # 한글 폰트 설정
import pandas as pd
# 데이터 변수 선언 ------------------------------------
TEMP_CSV = "../data/tem10y.csv"
# 데이터 준비 ------------------------------------------
df = pd.read_csv(TEMP_CSV, encoding="utf-8")
# 온도가 30도를 넘는 데이터 확인
hot_bool = (df["기온"] > 30)
# 데이터 추출
hot = df[hot_bool]
print(hot)
# 연별로 세기
cnt = hot.groupby(["연"])["연"].count()
print(cnt)
# 출력
font_path = r'C:\Windows\Fonts\malgun.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rc('axes', unicode_minus=False)
cnt.plot()
plt.title("tem-over30.png")
plt.savefig("tem-over30.png")
plt.show()