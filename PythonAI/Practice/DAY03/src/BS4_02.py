from bs4 import BeautifulSoup
# ID를 부여함

# 분석하고 싶은 HTML
html = """
<html>
    <title>Hello</title>
    <body>
        <h1 id="title">스크레이핑이란?</h1>
        <p id="body">웹페이지를 분석하는 것</p>
        <p id="title">원하는 부분을 추출하는 것</p>
    </body>
</html>
"""
# html 문자열을  html.parser로 파싱한다.
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출하기
t = soup.find_all(id="title")
b = soup.find(id="body")
print(t)
for i in t:
    print(i.string)
print("#body  : ",b.string)
