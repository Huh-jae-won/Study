import pandas as pd
import numpy as np
import tensorflow as tf

# csv파일 읽어오기
csv = pd.read_csv("../../DAY07/data/bmi.csv")

# 데이터 정규화
csv["height"] /= 200
csv["weight"] /= 100

# 레이블을 배열로 변환
# thin=[1,0,0], normal=[0,1,0], fat=[0,0,1]
bclass = {'thin':[1,0,0], 'normal':[0,1,0], 'fat':[0,0,1]}
csv['label_pat'] = csv["label"].apply(lambda x:np.array(bclass[x]))
print(csv)

# 테스트를 위한 데이터 분류
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])
# print("pat\n",test_pat)
# print("ans\n",test_ans)

# 데이터 플로우 그래프 구축
# 플레이스홀더 선언
x_ = tf.placeholder(tf.float32, [None,2])  # 키와 몸무게 데이터 용
y_ = tf.placeholder(tf.float32, [None,3])  # 정답 레이블(3종류) 용

# 변수 선언
W = tf.Variable(tf.zeros([2,3]))    # 가중치
b = tf.Variable(tf.zeros([3]))      # 바이어스
# 소프트맥스 회귀 정의
y = tf.nn.softmax(tf.matmul(x_, W)+b)
# matmul : 집합 곱 연산

# 모델 훈련
# 예상label : y
# 정답label : y_
cross_entropy = -tf.reduce_sum(y_*tf.log(y))    # 교차엔트로피가 적을수록 정확한 값을 나타냄
optimizer = tf.train.GradientDescentOptimizer(0.01) # 학습계수:0.01
train = optimizer.minimize(cross_entropy)
# 텐서플로가 알아서 가중치W와 바이어스b를 변경해줌

# 정답률 구하기
predict = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

# 세션 시작
sess = tf.Session()
sess.run(tf.global_variables_initializer()) # 변수 초기화
# 학습 시키기
for step in range(3500):
    i = (step*100)%14000
    rows = csv[1+i:1+i+100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x_:x_pat, y_:y_ans}
    sess.run(train,feed_dict=fd)
    if step%500==0 :
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x_:test_pat, y_:test_ans})
        print("step =",step, "cre =",cre, "acc =",acc)

# 최종 정답률 구하기
acc = sess.run(accuracy,feed_dict={x_:test_pat,y_:test_ans})
print("정답률 :",acc)


