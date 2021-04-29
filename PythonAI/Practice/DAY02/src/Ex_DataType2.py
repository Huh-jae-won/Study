## 바이트는 0~255까지(16진수로 두자리)
# 수정 불가
b1 = bytes(3)           # 3개짜리 생성
b2 = bytes([1,255])      # 시퀀스 객체
b3 = bytes(b'Happy')    # 바이트 객체
print(b1)
print(b2)
print(b3)
# 수정 가능
ba1 = bytearray(3)      #  빈 bytearray 생성 가능
ba2 = bytearray([1,2])
ba2[1]=3
print(ba2)
ba3 = bytearray(b'HAPPY')
print(chr(ba3[0]))      # chr():아스키코드로 <-> ord():아스키코드를 숫자로