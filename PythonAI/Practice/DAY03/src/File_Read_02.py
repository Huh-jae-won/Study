# file IO
FILE_NAME = "..\\data\\my_html.html"

with open(FILE_NAME,mode='r',encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line : break
        print(type(line),line, end="")
print("END")