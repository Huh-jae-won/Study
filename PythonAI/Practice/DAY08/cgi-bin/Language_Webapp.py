import cgi, os.path
import codecs, sys
import joblib

# http://localhost:8080/cgi-bin/Language_Webapp.py

# 표준 출력 인코딩 설정
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# 검출기 로딩
pklfile = os.path.dirname(__file__)+"./freq.pkl"
clf = joblib.load(pklfile)

def show_form(text,msg=""):
    print("Content-Type: text/html; charset=utf-8")
    print(""" 
        <!DOCTYPE html> 
        <html lang="en"> 
        <head> 
        <meta charset="UTF-8"> 
        <title>언어판별</title></head> 
        <body><form> 
        <textarea name="text" rows="8" cols="40"> {0} </textarea> 
        <p><input type="submit" value="판정"></p> 
        <p> {1} </p> 
        </form></body></html> 
        """.format(cgi.html.escape(text), msg))
def detect_lang(text):
    # 알파벳 출현빈도 구하기
    text = text.lower()
    code_a, code_z = (ord("a"), ord("z"))
    cnt = [0 for i in range(26)]
    for ch in text:
        n = ord(ch) - code_a
        if 0 <= n < 26: cnt[n] += 1
        total = sum(cnt)
        if total == 0: return "입력이 없습니다"
        freq = list(map(lambda n: n/total, cnt))
        res = clf.predict([freq])
    # 언어코드를 한국어로 변환하기
    lang_dic = {"en":"영어","fr":"프랑스어","id":"인도네시아어", "tl":"타갈로그어"}
    return lang_dic[res[0]]

# web 입력 양식 값 읽어 들이기
form = cgi.FieldStorage()
text = form.getvalue("text",default="")
print("text=>{}".format(text))
msg=""
if text !="":
    lang = detect_lang(text)
    msg = "판정 결과 : "+lang
    print("msg =:{}".format(msg))

# 입력 양식 결과 출력
show_form(text,msg)