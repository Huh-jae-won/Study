from sklearn import svm, metrics
import glob, os.path, re, json
import joblib

def check_freq(fname):
    name = os.path.basename(fname)  # 파일명만 추출
    # 조건'알파벳 2개이상으로 시작'과 일치하는 문자열 리턴
    lang = re.match(r'^[a-z]{2,}',name).group()

    with open(fname,"r",encoding='utf-8')as f :
        text = f.read()
    text = text.lower()
    # 숫자세기 변수(cnt) 초기화
    cnt = [0 for n in range(26)]
    code_a = ord('a')
    code_z = ord('z')
    # 알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z :
            cnt[n-code_a] += 1

    # 정규화 하기
    total = sum(cnt)
    freq = list(map(lambda n : n/total,cnt))    # 빈도로
    return (freq,lang)

def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs,"labels":labels}

#####
data = load_files("../data/train/*.txt")
test = load_files("../data/test/*.txt")

# 이후를 대비해서 JSON으로 결과 저장
with open("../data/freq.json",'w',encoding='utf-8') as fp :
    json.dump([data,test], fp)

# 학습
clf = svm.SVC()
clf.fit(data["freqs"],data["labels"])

predict = clf.predict(test["freqs"])

# 결과 테스트
ac_score = metrics.accuracy_score(test["labels"],predict)
cl_report = metrics.classification_report(test["labels"],predict)
print("정답률 :",ac_score)
print("리포트 :")
print(cl_report)

