# 변수 선언 ---------------------
msg='Hello'

# 문자열 포맷팅 ---------------------------
print('안녕하세요. {0:<10}님! 좋은 하루되세요.' .format('Happy') )
print('안녕하세요. {0:>10}님! 좋은 하루 되세요.' .format('appy') )
print('안녕하세요. {0:^10}님! 좋은 하루 되세요.' .format('Happy') )
print('안녕하세요. {0:=^10}님! 좋은 하루 되세요.' .format('Happy') )
print('안녕하세요. {:*>20.5f}님! 좋은 하루 되세요.'.format(12.12345678) )