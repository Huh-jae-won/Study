from keras.layers.core import Dense, Dropout, Activation
from keras.models import Sequential
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 데이터 가져오기
csv = pd.read_csv("../data/bmi.csv")
csv['weight'] /= 100
csv['height'] /= 200
X = csv[["weight","height"]]    # 원하는 열 추출

# 레이블
bclass = {'thin':[1,0,0], 'normal':[0,1,0], 'fat':[0,0,1]}
y = np.empty((20000,3))
for i,v in enumerate(csv['label']):
    y[i] = bclass[v]

# 훈련용, 테스트용 데이터 분리
X_train, y_train = X[1:15001], y[1:15001]
X_test, y_test = X[15001:], y[15001:]

# 모델 정의
model = Sequential()
model.add(Dense(512,input_shape=(2,)))
model.add(Activation("relu"))
model.add(Dropout(0.1))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(3))
model.add(Activation('softmax'))

# 모델 구축
model.compile(
    loss = 'categorical_crossentropy',
    optimizer = 'rmsprop',
    metrics = ['accuracy']
)

# 데이터 훈련
hist = model.fit(
    X_train,y_train, batch_size=100, epochs=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss',patience=2)],   # 모니터링 하는것 val_loss:오차율
    verbose=1
)

# 테스트 데이터로 평가
score = model.evaluate(X_test,y_test)
print('loss:',score[0])
print('accuracy:',score[1])