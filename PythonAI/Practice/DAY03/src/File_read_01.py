# file IO
FILE_NAME = "..\\data\\my_html.html"

try:
    file = open(FILE_NAME,mode='r',encoding='utf-8')
    while True:
        line = file.readline()
        if not line : break
        print(type(line),line,end="")
finally:
    file.close()