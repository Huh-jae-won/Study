import tensorflow as tf

# 상수 정의
a = tf.constant(200)
b = tf.constant(1000)

# 계산 정의
add_op = a + b  
# add_op 에는 상수가 아니라 데이터플로우그래프 객체가 대입됨

# 세션 시작
sess = tf.Session()
res = sess.run(add_op)  # 데이터플로우그래프를 run()의 매개변수로 전달
print(res)

# 계산 프로그램을 그래프라는 객체로 구축하고
# 이 그래프를 실행(by run())