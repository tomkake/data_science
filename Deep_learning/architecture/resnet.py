from keras.datasets import cifar10
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
cifar10_labels = [
    'airplane',
    'automobile',
    'bird',
    'cat',
    'deer',
    'dog',
    'frog',
    'horse',
    'ship',
    'truck'
]

plt.imshow(X_train[1])
plt.axis('off')
plt.title(cifar10_labels[y_train[1][0]])
plt.tight_layout()

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255.
X_test /= 255.

from keras.utils import np_utils

# クラスラベルのone-hot-vector化
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.layers import Conv2D,MaxPool2D,Input,add,BatchNormalization,GlobalAveragePooling2D,MaxPooling2D
from keras.models import Model
from keras.optimizers import Adam
from keras.layers.core import Dense, Activation, Dropout, Flatten
from tensorflow.python.keras.callbacks import TensorBoard

def short_cut(x ,residual):
  """畳み込んだものと、入ってきたデータの残渣関数をくっつける。"""
  strides=(1,1)
  n_filters = residual._keras_shape[3]
  x = Conv2D(n_filters , (1,1), strides = strides,padding='valid')(x)
  return add([x , residual])

def residual_block(n_filters):
  def input_pack(input_data):
    strides = (1,1)
    x_before = Conv2D(n_filters , (3,3),strides = strides,kernel_initializer='he_normal', padding='same')(input_data)
    x = BatchNormalization()(x_before)
    x = Activation('relu')(x)
    x = Conv2D(n_filters , (3,3),strides = strides,kernel_initializer='he_normal', padding='same')(x)
    x = BatchNormalization()(x)
    return short_cut(input_data , x)
  return input_pack

def resnet():
  inputs = Input(shape=(32, 32, 3))
  x = Conv2D(32, (7,7), strides=(1,1),
                    kernel_initializer='he_normal', padding='same')(inputs)
  x = BatchNormalization()(x)
  x = Activation('relu')(x)
  x = MaxPooling2D((3, 3), strides=(2,2), padding='same')(x)


  x = residual_block(n_filters=64)(x)
  x = residual_block(n_filters=64)(x)
  x = residual_block(n_filters=64)(x)
  x = MaxPooling2D(strides=(2,2))(x)  
  x =residual_block(n_filters=128)(x)
  x =residual_block(n_filters=128)(x)
  x = residual_block(n_filters=128)(x)


  x = GlobalAveragePooling2D()(x)
  x = Dense(10, kernel_initializer='he_normal', activation='softmax')(x)

  model = Model(inputs=inputs, outputs=x)
  return model

model = resnet()

adam = Adam()

model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

fit = model.fit(X_train,y_train,batch_size = 256 , verbose = 2,validation_split = 0.2,epochs = 100)



from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

SVG(model_to_dot(model).create(prog='dot', format='svg'))

score = model.evaluate(X_test, y_test,
                    verbose=0
                    )

print('Test accuracy:', score[1])

# ----------------------------------------------
# Some plots
# ----------------------------------------------
fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))

# loss
def plot_history_loss(fit):
    # Plot the loss in the history
    axL.plot(fit.history['loss'],label="loss for training")
    axL.plot(fit.history['val_loss'],label="loss for validation")
    axL.set_title('model loss')
    axL.set_xlabel('epoch')
    axL.set_ylabel('loss')
    axL.legend(loc='upper right')

# acc
def plot_history_acc(fit):
    # Plot the loss in the history
    axR.plot(fit.history['acc'],label="loss for training")
    axR.plot(fit.history['val_acc'],label="loss for validation")
    axR.set_title('model accuracy')
    axR.set_xlabel('epoch')
    axR.set_ylabel('accuracy')
    axR.legend(loc='upper right')

plot_history_loss(fit)
plot_history_acc(fit)
plt.show()
plt.close()

