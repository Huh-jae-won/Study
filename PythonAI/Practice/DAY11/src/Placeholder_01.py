import tensorflow as tf

# 플레이스홀더 정의
a = tf.placeholder(tf.int32, [3])       # 정수자료형 3개공간 설정
x = tf.placeholder(tf.int32, [None])    # 공간 갯수 지정x
# 상수 정의
b = tf.constant(2)
c = tf.constant(10)

# 데이터 플로우 그래프 정의
mul_op = a*b        # a값을 모두 b배 하는 연산
x10_op = x*c

# 세션시작
sess = tf.Session()

# 플레이스홀데어 값을 넣고 실행
r1 = sess.run(mul_op,feed_dict={a:[1,2,3]})
r2 = sess.run(mul_op,feed_dict={a:[11,22,33]})
n1 = sess.run(x10_op,feed_dict={x:[1]})
n2 = sess.run(x10_op,feed_dict={x:[0,10,20]})
print(r1)
print(r2)
print(n1)
print(n2)