import matplotlib.pyplot as plt
import pandas as pd
import json

# 알파벳 빈도 데이터 읽어오기
with open("../data/freq.json",'r',encoding='utf-8') as fp :
    freq = fp.load(fp)
# 언어 마다 계산하기
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]    # train용 데이터 추출
    if not(lbl in lang_dic):    # 레이블 언어 데이터 채우기
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):                        # 언어별 알파벳 26개 빈도값 채우기
        lang_dic[lbl][idx] = (lang_dic[lbl][idx]+v)/2   # 0~1사이값으로 범위 한정

# pandas의 dataframe에 데이터 넣기
asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)

# 그래프그리기
plt.style.use('ggplot')
df.plot(kind='bar',subplots=True,ylim=(0,0.15))
plt.savefig("lang-plot.png")
