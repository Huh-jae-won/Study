from urllib.parse import urljoin

base = "http://example.com/html/a.html"
# 상대경로
print(urljoin(base,"b.html"))
print(urljoin(base,"sub/c.html"))
print(urljoin(base,"../index.html"))
# 절대경로
print(urljoin(base, "http://otherExample.com/wiki"))
print(urljoin(base, "//anotherExample.org/test"))
print(base)