FILE_NAME = "..\\data\\ex_write.txt"
try:
    # mode가 a면 append, w는 덮어쓰기
    file = open(FILE_NAME,mode='a',encoding='utf-8')
    for i in range(1,6):
        data = "%d째줄\n" %i
        file.write(data)
finally:
    file.close()