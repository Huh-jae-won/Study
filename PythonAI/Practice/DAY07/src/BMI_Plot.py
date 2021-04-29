import matplotlib.pyplot as plt
from matplotlib import font_manager as fm   # 한글 폰트 설정
import pandas as pd

# 한글 폰트 설정 ---------------------------------------
font_path = r'C:\Windows\Fonts\malgun.ttf'  # 맑은 고딕
font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
plt.rc('font', family=font_name)     # mpl.rcParams['font.family'] = 'Gullim'
plt.rc('axes', unicode_minus=False)  # mpl.rcParams['axes.unicode_minus'] = False
# -----------------------------------------------------

tbl = pd.read_csv("../data/bmi.csv",index_col=2)    # 2(0,1,2中)를 행의 인덱스로 사용하겠다
print(tbl)
# 분포도 그래프 그리기
plt.scatter(tbl.loc["fat"]["height"], tbl.loc["fat"]["weight"], c='red', marker='x',label="fat")
plt.scatter(tbl.loc["normal"]["height"], tbl.loc["normal"]["weight"], c='green', marker='v',label="normal")
plt.scatter(tbl.loc["thin"]["height"], tbl.loc["thin"]["weight"], c='yellow', label="thin")
plt.title("-분포도")
plt.suptitle("BMI")

# 그래프 저장
plt.savefig("../data/BMI_Test.png")

plt.show()



