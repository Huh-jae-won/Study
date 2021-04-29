import urllib.request

#URL과 저장경로 지정
url = 'http://uta.pw/shodou/img/28/214.png'
savename = '..\\data\\text.png'

# 다운로드
mem = urllib.request.urlopen(url).read()
# 받아온 파일은 바이너리 형식

# 파일로 저장
with open(savename,mode='ab') as file :
    file.write(mem)
print("저장되었습니다.")