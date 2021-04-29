# calculate.py - 4칙 연산 모듈

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def main():
    print(add(10, 10))

## __name__ :현재 실행되고있는 파일의 이름이 저장되있음
if __name__=='__main__':
    ## 이 파일이 실행될때만 실행될 코드들
    ## 바깥은 모듈로서 사용될 때
    print('__name__ =>', __name__)
    main()
