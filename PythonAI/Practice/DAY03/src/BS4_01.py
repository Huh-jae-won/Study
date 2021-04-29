from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html>
    <title>Hello</title>
    <body>바디
        <h1>스크레이핑이란?</h1>
        <p>웹페이지를 분석하는 것</p>
        <p>원하는 부분을 추출하는 것</p>
    </body>
</html>
"""
# html 문자열을  html.parser로 파싱한다.
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 태그추출
t1 = soup.html.title
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
# <p>의 넥스트는</P>, </p>의 넥스트는 아래 <p>
# next_sibling : 같은 이름의 태그를 찾는
b1 = soup.html.body

# 요소의 글자 출력
print("t1 = ",t1.string)
print("h1 = ",h1.string)
print("b1 = ",b1.string)
print("p1 = ",p1.string)
print("p2 = ",p2.string)
