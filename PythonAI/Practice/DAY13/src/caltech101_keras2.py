from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import h5py
from PIL import Image
import numpy as np
import os


# 데이터 변수 선언 -----------------------------------------------
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)
image_w = 64 
image_h = 64


# 데이터 준비 ----------------------------------------------------
X_train, X_test, y_train, y_test = np.load("../DATA/5obj.npy")
# 데이터 정규화
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)

# 모델 구축하기 --------------------------------------------------
model = Sequential()
model.add(Convolution2D(32, 3, 3, 
    border_mode='same',
    input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten()) # --- (※3) 
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

# 모델 생성
model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

# 모델 훈련하기 -------------------------------------------------
hdf5_file = "../DATA/5obj-model.hdf5"
if os.path.exists(hdf5_file):
    model.load_weights(hdf5_file)
else:
    model.fit(X_train, y_train, batch_size=32, nb_epoch=50)
    model.save_weights(hdf5_file)

# 모델 평가 -------------------------------------------------------
pre = model.predict(X_test)
for i,v in enumerate(pre):
    pre_ans = v.argmax()
    ans = y_test[i].argmax()
    dat = X_test[i]
    if ans == pre_ans: continue
    print("[NG]", categories[pre_ans], "!=", categories[ans])
    print(v)
    fname = "image/error/" + str(i) + "-" + categories[pre_ans] + \
        "-ne-" + categories[ans] + ".png"
    dat *= 256
    img = Image.fromarray(np.uint8(dat))
    img.save(fname)
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])


