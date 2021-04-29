import tensorflow as tf

# 상수 정의
a = tf.constant(120, name='a')
b = tf.constant(120, name='b')
c = tf.constant(120, name='c')

# 변수 정의
v = tf.Variable(0, name='vv')

# 데이터 플로우 그래프 정의
calc_op = a+b+c
assign_op = tf.assign(v,calc_op)    # v에 calc_op연산을 대입
    # 변수에 값을 대입(저장)하는 방법?

# 세션 시작
sess = tf.Session()
sess.run(assign_op)

# v내용 출력
print(sess.run(v))  # assign_op를 먼저run해줘야함