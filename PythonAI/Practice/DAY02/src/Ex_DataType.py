
msg = "hello"
## 문자열 길이
print(len(msg))

## 인덱싱
for i in range(len(msg)):
    print(msg[i]+" ",end="")

print()
for i in range(-1,-(len(msg)+1),-1):
    print(msg[i]+" ",end="")
print()

# msg[2] = "a" 문자열은 요소변경 불가
msg = msg[0]+ "a" + msg[2:] # 억지로 바꾸는 방법
print(msg)

str = "Happy New Year"
## 문자열 나누기
data1 = str.split(" ")
print("문자열 나누기 : ",data1)
##  문자열 합치기
data2 = ",".join(data1)
print("문자열(리스트) 합치기 : ",data2)

## 문자열 치환
new_str = str.replace("e","E")
print("문자열 치환 : ",new_str)

## Formatting
day = 4
month = 2
year = 2020
msg = "I like {1}year {0}month {2}day".format(month,year,day)
print("Formatting : ",msg)