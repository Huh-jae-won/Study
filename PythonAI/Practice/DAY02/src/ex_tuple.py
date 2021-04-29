# 튜플 선언 ------------------------------------------
# 보통 함수 리턴값으로 사용함(변경되면 안되므로)
print('\n튜플 선언 ====================')
t0=('A',)
t1=(1,2,'a','b')
t2='a','b','c'
t3='2020',

print('t0 = {}, len(t0)= {}, type(t0) = {}'.format(t0, len(t0), type(t0)))
print('t1 = {}, len(t1)= {}, type(t1) = {}'.format(t1, len(t1), type(t1)))
print('t2 = {}, len(t2)= {}, type(t2) = {}'.format(t2, len(t2), type(t2)))
print('t3 = {}, len(t3)= {}, type(t3) = {}'.format(t3, len(t3), type(t3)))

print('\n {} 튜플 인덱싱 & 슬라이싱 ===================='.format(t1))
print('t1[0]={}, t1[len(t1)-1]={}'.format(t1[0], t1[len(t1)-1]))
print('t1[:2] = {}, t1[:-2]={}'.format(t1[:2], t1[1:-2]))
